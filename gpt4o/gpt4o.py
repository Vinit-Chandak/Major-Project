import json
import time
import requests
from google.cloud import storage

# ------------------ Configuration ------------------
PROJECT_ID = "major-project-vinit"
LOCATION = "asia-southeast1"
IMAGE_BUCKET_NAME = "test_bucket-iitd"
JSON_FILE_PATH = "qa_pairs.json"
OPENAI_API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
API_KEY = ""

# Rate Limiting
TIME_BETWEEN_REQUESTS = 0  # Seconds
BLOCK_SIZE = 100  # Number of images per block
START_IMAGE_INDEX = 811  # Change this value to the desired starting image index

# -------- Function to Check Image Index --------
def is_image_index_ends_with_one(image_index):
    return str(image_index).endswith('1')

# -------- Function to construct the public URL --------
def get_gcs_public_url(bucket_name, image_filename):
    return f"https://storage.googleapis.com/{bucket_name}/{image_filename}"

# -------- Function to Process a Single Image --------
def process_image(image_url, question, api_endpoint, api_key):
    print("Processing image:", image_url)  # Debug

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }
        ],
        "max_tokens": 300
    }

    try:
        response = requests.post(api_endpoint, headers=headers, json=payload)
        response.raise_for_status()
        response_json = response.json()
        print(response_json)  # Debug

        answer_text = response_json['choices'][0]['message']['content']
        is_answer_yes = answer_text.lower().startswith("yes")
        print("Extracted Answer:", is_answer_yes)  # Debug
    except (requests.exceptions.RequestException, IndexError, KeyError) as e:
        print("OpenAI API error or unexpected format. Error:", e)
        is_answer_yes = False  # Default in case of error

    return is_answer_yes

# -------- Function to Analyze and Save Results --------
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
        # Create GCS public URL
        image_url = get_gcs_public_url(IMAGE_BUCKET_NAME, image_filename)
        is_answer_yes = process_image(image_url, item['question_string'], api_endpoint, api_key)
        item['gpt4o_answer'] = 1 if is_answer_yes else 0

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

image_indices = [item['image_index'] for item in figureqa_data['qa_pairs'][start_index:] if
                 is_image_index_ends_with_one(item['image_index'])]
total_images = len(image_indices)

for block_num in range(0, total_images, BLOCK_SIZE):
    start_block_index = start_index + block_num
    end_index = min(start_block_index + BLOCK_SIZE, len(figureqa_data['qa_pairs']))
    analyze_and_save(JSON_FILE_PATH, OPENAI_API_ENDPOINT, API_KEY, start_block_index, end_index)