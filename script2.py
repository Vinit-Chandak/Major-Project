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
GEMINI_PRO_VISION_API_ENDPOINT = "https://{asia-southeast1}-aiplatform.googleapis.com/v1/projects/{gen-lang-client-0607931977}/locations/{asia-southeast1}/publishers/google/models/gemini-1.0-pro-vision:streamGenerateContent"
API_KEY = ""

# Rate Limiting 
TIME_BETWEEN_REQUESTS = 0  # Seconds
BLOCK_SIZE = 100  # Number of images per block

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

def analyze_dataset(json_file_path, api_endpoint, api_key):
    print("JSON File Path:", json_file_path) # Debug
    with open(json_file_path) as f:
        print("JSON file opened successfully")  # Debug
        figureqa_data = json.load(f)
        print("JSON data loaded")  # Debug

    storage_client = storage.Client()

    # Create a new list to store analyzed data
    analyzed_data = [] 
    
    max_requests = 10  # Set the maximum requests
    requests_count = 0

    for item in figureqa_data['qa_pairs']:  # Access the list within 'qa_pairs' 
        print("Processing Item:", item)  # Debug
        image_index = item['image_index']
        image_filename = f"{image_index}.png"
        image_url = f"gs://{IMAGE_BUCKET_NAME}/{image_filename}" 

        is_answer_yes = process_image(image_url, item['question_string'], api_endpoint, api_key)
        
        # Store 0 or 1 based on the answer
        item['gemini_answer'] = 1 if is_answer_yes else 0

        # Add the updated item to the analyzed_data list
        analyzed_data.append(item) 

        requests_count += 1
        if requests_count >= max_requests:
            break  # Stop after max_requests

        time.sleep(TIME_BETWEEN_REQUESTS)  # Enforce waiting

    
    return analyzed_data   

# -------- Main Execution -------- 
analyzed_data = analyze_dataset(JSON_FILE_PATH, GEMINI_PRO_VISION_API_ENDPOINT, API_KEY)

total_images = len(figureqa_data['qa_pairs'])

for block_num in range(0, total_images, BLOCK_SIZE):
    start_index = block_num
    end_index = min(block_num + BLOCK_SIZE, total_images)  # Handle last block

    analyzed_data = analyze_block(JSON_FILE_PATH, GEMINI_PRO_VISION_API_ENDPOINT, API_KEY, start_index, end_index)

    # Save block results
    filename = f'figureqa_analyzed_block_{block_num // BLOCK_SIZE + 1}.json' 
    with open(filename, 'w') as f:
        json.dump(analyzed_data, f)  
        print(f"Analysis Results Saved for Block {block_num // BLOCK_SIZE + 1} ({filename})")