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
API_KEY = "sk-proj-OZ0oEYNJYG49SU8yr9hzT3BlbkFJS6Sqi3PJGzsXveUAILyk"

# Rate Limiting
TIME_BETWEEN_REQUESTS = 0  # Seconds
BLOCK_SIZE = 100  # Number of images per block

# Function to construct the public URL
def get_gcs_public_url(bucket_name, image_filename):
    return f"https://storage.googleapis.com/{bucket_name}/{image_filename}"

# Function to process a single image
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

    response = requests.post(api_endpoint, headers=headers, json=payload)
    response_json = response.json()
    print(response_json)  # Debug

    try:
        answer_text = response_json['choices'][0]['message']['content']
        is_answer_yes = answer_text.lower().startswith("yes")
        print("Extracted Answer:", is_answer_yes)  # Debug
    except (IndexError, KeyError) as e:
        print("OpenAI did not return an answer or returned an unexpected format. Error:", e)
        is_answer_yes = False  # Default in case of error

    return is_answer_yes

# Function to analyze and save results
def analyze_and_save(json_file_path, api_endpoint, api_key, start_index, end_index):
    print("JSON File Path:", json_file_path) # Debug
    with open(json_file_path) as f:
        print("JSON file opened successfully")  # Debug
        figureqa_data = json.load(f)
        print("JSON data loaded")  # Debug

    analyzed_data = []

    for item in figureqa_data['qa_pairs'][start_index:end_index]:  # Process a slice of the dataset
        print("Processing Item:", item)

        image_index = item['image_index']
        image_filename = f"{image_index}.png"
        # Create GCS public URL
        image_url = get_gcs_public_url(IMAGE_BUCKET_NAME, image_filename)

        is_answer_yes = process_image(image_url, item['question_string'], api_endpoint, api_key)
        item['gpt4o_answer'] = 1 if is_answer_yes else 0
        analyzed_data.append(item)
        time.sleep(TIME_BETWEEN_REQUESTS)

    for image_index in set(item['image_index'] for item in analyzed_data):
        output_filename = f'figureqa_analyzed_image_{image_index}.json'
        with open(output_filename, 'w') as f:
            json.dump([d for d in analyzed_data if d['image_index'] == image_index], f)
        print(f"Analysis Results Saved for Image {image_index} ({output_filename})")

# Main Execution
with open(JSON_FILE_PATH) as f:
    figureqa_data = json.load(f)

total_images = len(figureqa_data['qa_pairs'])

for block_num in range(0, total_images, BLOCK_SIZE):
    start_index = block_num
    end_index = min(block_num + BLOCK_SIZE, total_images)
    analyze_and_save(JSON_FILE_PATH, OPENAI_API_ENDPOINT, API_KEY, start_index, end_index)
