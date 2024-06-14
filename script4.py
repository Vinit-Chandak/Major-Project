import vertexai
from vertexai.generative_models import GenerativeModel, Part
import json
import time
import requests
from google.cloud import storage

# ------------------ Configuration ------------------
PROJECT_ID = "major-project-vinit"
LOCATION = "asia-southeast1"
IMAGE_BUCKET_NAME = "test_bucket-iitd"
JSON_FILE_PATH = "qa_pairs.json"
GEMINI_PRO_VISION_API_ENDPOINT = "https://{asia-southeast1}-aiplatform.googleapis.com/v1/projects/{major-project-vinit}/locations/{asia-southeast1}/publishers/google/models/gemini-1.5-pro:streamGenerateContent"
API_KEY = ""

# --------- Rate Limiting -----------
TIME_BETWEEN_REQUESTS = 12  # Seconds (5 requests per minute)
BLOCK_SIZE = 100  # Number of images per block
START_IMAGE_INDEX = 811 # Change this value to the desired starting image index

# -------- Function to Check Image Index --------
def is_image_index_ends_with_one(image_index):
    return str(image_index).endswith('1')

# -------- Function to Process a Single Image --------
def process_image(image_url, question, api_endpoint, api_key):
    print("Processing image:", image_url)  # Debug
    # Initialize Vertex AI
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    multimodal_model = GenerativeModel("gemini-1.5-pro-preview-0409")
    response = multimodal_model.generate_content([
        Part.from_uri(image_url, mime_type="image/png"),
        question
    ])
    print("Gemini Response:", response)  # Debug
    try:
        answer_text = response.candidates[0].content.parts[0].text
        is_answer_yes = "yes" in answer_text.lower()
        print("Extracted Answer:", is_answer_yes)  # Debug
    except IndexError:
        # Handle cases with no candidates gracefully
        print("Gemini did not return an answer (possible safety filtering)")
        is_answer_yes = False  # Set a default
    return is_answer_yes

def analyze_and_save(json_file_path, api_endpoint, api_key, start_index, end_index):
    print("JSON File Path:", json_file_path)  # Debug
    with open(json_file_path) as f:
        print("JSON file opened successfully")  # Debug
        figureqa_data = json.load(f)
        print("JSON data loaded")  # Debug

    storage_client = storage.Client()
    image_results = {}

    for item in figureqa_data['qa_pairs'][start_index:end_index]:
        image_index = item['image_index']
        if not is_image_index_ends_with_one(image_index):
            continue

        image_filename = f"{image_index}.png"
        image_url = f"gs://{IMAGE_BUCKET_NAME}/{image_filename}"
        is_answer_yes = process_image(image_url, item['question_string'], api_endpoint, api_key)
        item['gemini_answer'] = 1 if is_answer_yes else 0

        if image_index not in image_results:
            image_results[image_index] = []

        image_results[image_index].append(item)

        time.sleep(TIME_BETWEEN_REQUESTS)

    for image_index, results in image_results.items():
        filename = f'figureqa_analyzed_image_{image_index}.json'
        with open(filename, 'w') as f:
            json.dump(results, f)
        print(f"Analysis Results Saved for Image {image_index} ({filename})")

# -------- Main Execution --------
with open(JSON_FILE_PATH) as f:
    figureqa_data = json.load(f)

start_index = next((i for i, item in enumerate(figureqa_data['qa_pairs']) if item['image_index'] >= START_IMAGE_INDEX), 0)

image_indices = [item['image_index'] for item in figureqa_data['qa_pairs'][start_index:] if is_image_index_ends_with_one(item['image_index'])]
total_images = len(image_indices)

for block_num in range(0, total_images, BLOCK_SIZE):
    start_block_index = start_index + block_num
    end_index = min(start_block_index + BLOCK_SIZE, len(figureqa_data['qa_pairs']))
    analyze_and_save(JSON_FILE_PATH, GEMINI_PRO_VISION_API_ENDPOINT, API_KEY, start_block_index, end_index)