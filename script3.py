import vertexai
from vertexai.generative_models import GenerativeModel, Part
import json
import time
import requests  
from google.cloud import storage

# ------------------ Configuration ------------------
PROJECT_ID = "gen-lang-client-0607931977" 
LOCATION = "asia-southeast1"
IMAGE_BUCKET_NAME = "test_bucket-iitd"
JSON_FILE_PATH = "qa_pairs.json"
GEMINI_PRO_VISION_API_ENDPOINT = "https://{asia-southeast1}-aiplatform.googleapis.com/v1/projects/{gen-lang-client-0607931977}/locations/{asia-southeast1}/publishers/google/models/gemini-1.5-pro:streamGenerateContent"
API_KEY = "AIzaSyA9dxGDTyuxze6VzNNhpCxPrx-zGO1YjWA"

# Rate Limiting 
TIME_BETWEEN_REQUESTS = 0 # Seconds
BLOCK_SIZE = 100 # Number of images per block

# -------- Function to Process a Single Image --------
def process_image(image_url, question, api_endpoint, api_key):
    print("Processing image:", image_url)  # Debug

    # Initialize Vertex AI
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")

    response = multimodal_model.generate_content([
        Part.from_uri(image_url, mime_type="image/png"),
        question
    ])

    print("Gemini Response:", response)  # Debug

    try:
        answer_text = response.candidates[0].content.parts[0].text
        is_answer_yes = "yes" in answer_text.lower()  
        print("Extracted Answer:", is_answer_yes) # Debug
    except IndexError:  # Handle cases with no candidates gracefully
        print("Gemini did not return an answer (possible safety filtering)")
        is_answer_yes = False  # Set a default 

    return is_answer_yes

# -------- Function to Analyze and Save Results --------
def analyze_and_save(json_file_path, api_endpoint, api_key, start_index, end_index):
    print("JSON File Path:", json_file_path) # Debug
    with open(json_file_path) as f:
        print("JSON file opened successfully")  # Debug
        figureqa_data = json.load(f)
        print("JSON data loaded")  # Debug

    storage_client = storage.Client()
    analyzed_data = []

    for item in figureqa_data['qa_pairs'][start_index:end_index]: # Process a slice of the dataset 
        print("Processing Item:", item)  

        image_index = item['image_index']
        image_filename = f"{image_index}.png"
        image_url = f"gs://{IMAGE_BUCKET_NAME}/{image_filename}" 

        is_answer_yes = process_image(image_url, item['question_string'], api_endpoint, api_key)
        item['gemini_answer'] = 1 if is_answer_yes else 0 
        analyzed_data.append(item) 
        time.sleep(TIME_BETWEEN_REQUESTS)  

    # Save block results
    block_num = start_index // BLOCK_SIZE + 1 
    filename = f'figureqa_analyzed_block_{block_num}.json' 
    with open(filename, 'w') as f:
        json.dump(analyzed_data, f) 
        print(f"Analysis Results Saved for Block {block_num} ({filename})") 

# -------- Main Execution -------- 
with open(JSON_FILE_PATH) as f:
    figureqa_data = json.load(f)  

total_images = len(figureqa_data['qa_pairs'])

for block_num in range(0, total_images, BLOCK_SIZE):
    start_index = block_num
    end_index = min(block_num + BLOCK_SIZE, total_images)  
    analyze_and_save(JSON_FILE_PATH, GEMINI_PRO_VISION_API_ENDPOINT, API_KEY, start_index, end_index)
