import requests
import json
import os
from google.cloud import storage 
import io
from PIL import Image

GEMINI_PRO_VISION_API_ENDPOINT = "https://{asia-southeast1}-aiplatform.googleapis.com/v1/projects/{gen-lang-client-0607931977}/locations/{asia-southeast1}/publishers/google/models/gemini-1.0-pro-vision:streamGenerateContent"
API_KEY = "AIzaSyA9dxGDTyuxze6VzNNhpCxPrx-zGO1YjWA" 

IMAGE_BUCKET_NAME = "test_bucket-iitd"  # Replace with your bucket's name
JSON_FILE_PATH = "figureqa_analyzed.json"

def process_image(image_url, question, GEMINI_PRO_VISION_API_ENDPOINT, API_KEY):
    print("Processing image:", image_url)
    print(type(image_url))  # For debugging, you'll likely remove this later

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        with io.BytesIO(response.content) as image_stream:
            # ----- Image Processing with PIL (Example) -----
            image = Image.open(image_stream)

            # ***** Your image analysis logic here ***** 
            # Example - Simply get dimensions, but replace  with your analysis
            width, height = image.size
            print(f"Image dimensions: {width} x {height}") 

            # ----- API Interaction (Preserved as provided) -----
            headers = {'Authorization': f'Bearer {API_KEY}'}
            payload = {
                "contents": [
                    {
                        "role": "user", 
                        "parts": [
                            {
                                "fileData": {
                                    "mimeType": "image/png",  
                                    "fileUri": image_url
                                }
                            },
                            {
                                "text": question 
                            }
                        ]
                    }
                ]
            }
            print("API payload:", payload)

            api_response = requests.post(GEMINI_PRO_VISION_API_ENDPOINT, headers=headers, json=payload)
            print("API request sent with status code:", api_response.status_code)

            if api_response.status_code == 200:
                api_response_json = api_response.json()
                generated_response = api_response_json["contents"][0]['parts'][0]['text'] 
                print("API response:", generated_response)
                is_answer_yes = "yes" in generated_response.lower()
                return is_answer_yes
            else:
                print(f"API request failed with status code: {api_response.status_code}")
                return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during image download: {e}")
        return None
    except FileNotFoundError:  # Likely redundant now 
        print(f"Error: Image file not found: {image_url}") 
        return None
    except Exception as e:  
        print(f"An error occurred during image processing: {e}")
        return None

def analyze_figureqa_dataset(json_file_path, GEMINI_PRO_VISION_API_ENDPOINT, API_KEY):
    print("JSON file path:", json_file_path)
    try:
        with open(json_file_path) as f:
            print("JSON file opened successfully")
            figureqa_data = json.load(f)
            print("JSON data loaded")

        results = []
        storage_client = storage.Client()  

        for item in figureqa_data['qa_pairs']:
            try:
                image_index = item['image_index'] 
                image_filename = f"{image_index}.png"  
                print("Image filename:", image_filename) 
            except (ValueError, TypeError):
                print(f"Error: Invalid image_index ({item['image_index']}) - skipping image.")
                continue 

            image_blob = storage_client.bucket(IMAGE_BUCKET_NAME).get_blob(image_filename) 

            if image_blob:
                image_url = image_blob.public_url  
                is_answer_yes = process_image(image_url, item['question_string'], GEMINI_PRO_VISION_API_ENDPOINT, API_KEY)
            else:
                print(f"Error: Image {image_filename} not found in bucket.")
                is_answer_yes = None 

            item['gemini_answer'] = 'yes' if is_answer_yes else 'no'
            results.append(item)

        return results

    except FileNotFoundError:
        print("Error: JSON file not found.")
    except json.JSONDecodeError as e:
        print("Error: Invalid JSON format. Details:", e)

# Example usage
new_figureqa_data = analyze_figureqa_dataset(JSON_FILE_PATH, GEMINI_PRO_VISION_API_ENDPOINT, API_KEY)

# Save the updated data
with open('figureqa_analyzed.json', 'w') as f:
    json.dump(new_figureqa_data, f)

