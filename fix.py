import json

def fix_image_indices(json_file_path):
    print("JSON file path:", json_file_path)

    try:
        with open(json_file_path, 'r') as f:  
            print("File opened successfully")
            data = json.load(f)
            print("JSON data loaded")

            for item in data['qa_pairs']: 
                print("Processing item:", item)
                if isinstance(item['image_index'], str):  
                    print("image_index is a string:", item['image_index'])
                    try:
                        item['image_index'] = int(item['image_index'])  
                        print("Converted image_index to integer")
                    except ValueError:
                        print(f"Error: Could not convert image_index ({item['image_index']}) to integer - skipping")

        with open(json_file_path, 'w') as f: 
            print("Saving corrected JSON data") 
            json.dump(data, f)

        print("JSON file fix complete!")

    except FileNotFoundError:
        print("Error: JSON file not found at specified path.")
    except json.JSONDecodeError as e:
        print("Error: Invalid JSON format. Details:", e)


json_file_path = "figureqa-sample-train-v1/sample_train1/qa_pairs.json" 
fix_image_indices(json_file_path) 
