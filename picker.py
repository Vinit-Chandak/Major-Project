import os
import random
import json
import shutil

# Define the image types and their ranges
image_types = {
    "type1": range(1, 251),
    "type2": range(251, 501),
    "type3": range(501, 751),
    "type4": range(751, 1001)
}

# Read the original JSON file
with open("qa_pairs.json", "r") as f:
    data = json.load(f)["qa_pairs"]

# Create a new dictionary to store the selected data
new_data = {"qa_pairs": []}

# Create a new folder for the selected images
os.makedirs("selected_images", exist_ok=True)

# Iterate over the image types
for image_type, image_range in image_types.items():
    # Select 25 random images from the current type
    selected_images = random.sample(list(image_range), 25)

    # Add the selected images and their corresponding data to the new dictionary
    for qa_pair in data:
        image_id = qa_pair["image_index"] + 1  # Assuming image_index starts from 0
        if image_id in selected_images:
            new_data["qa_pairs"].append(qa_pair)

    # Copy the selected images to the new folder
    for image_id in selected_images:
        src = f"figureqa-sample-train-v1/sample_train1/png/{image_id}.png"
        dst = f"selected_images/{image_id}.png"
        shutil.copy(src, dst)

# Write the new data to a new JSON file
with open("new_data.json", "w") as f:
    json.dump(new_data, f, indent=2)