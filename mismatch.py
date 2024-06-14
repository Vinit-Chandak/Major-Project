import os
import json

# -------------------- Configuration --------------------
FOLDER1_PATH = "gemini-1.5-pro-subset"
FOLDER2_PATH = "gpt4o"
FILE_PREFIX = "figureqa_analyzed_image_"
FILE_EXTENSION = ".json"

# -------------------- Helper Functions --------------------

def get_files_with_prefix(directory, prefix, extension):
    """
    Returns a list of files in the directory that match the given prefix and extension.
    """
    return [f for f in os.listdir(directory) if f.startswith(prefix) and f.endswith(extension)]

def read_json_file(filepath):
    """
    Reads a JSON file and returns the data.
    """
    with open(filepath, 'r') as file:
        return json.load(file)

# -------------------- Main Execution --------------------

# Get list of files in both folders
files1 = get_files_with_prefix(FOLDER1_PATH, FILE_PREFIX, FILE_EXTENSION)
files2 = get_files_with_prefix(FOLDER2_PATH, FILE_PREFIX, FILE_EXTENSION)

# Sort the files to ensure we are comparing corresponding files
files1.sort()
files2.sort()

# Initialize lists to store mismatch information
missing_in_folder1 = []
missing_in_folder2 = []
entry_mismatches = []

# Check for missing files in both folders
for f in files1:
    if f not in files2:
        missing_in_folder2.append(f)

for f in files2:
    if f not in files1:
        missing_in_folder1.append(f)

# Check for entry mismatches
for f in set(files1).intersection(files2):
    file1_path = os.path.join(FOLDER1_PATH, f)
    file2_path = os.path.join(FOLDER2_PATH, f)

    data1 = read_json_file(file1_path)
    data2 = read_json_file(file2_path)

    if len(data1) != len(data2):
        entry_mismatches.append(f)
        continue

    for entry1, entry2 in zip(data1, data2):
        if entry1['question_string'] != entry2['question_string']:
            entry_mismatches.append(f)
            break

# Print results
print("Missing Files Report:")
if missing_in_folder1:
    print("\nFiles present in Folder 2 but missing in Folder 1:")
    for f in missing_in_folder1:
        print(f)
else:
    print("\nNo files are missing in Folder 1.")

if missing_in_folder2:
    print("\nFiles present in Folder 1 but missing in Folder 2:")
    for f in missing_in_folder2:
        print(f)
else:
    print("\nNo files are missing in Folder 2.")

print("\nEntry Mismatch Report:")
if entry_mismatches:
    print("\nFiles with mismatched entries:")
    for f in entry_mismatches:
        print(f)
else:
    print("\nNo files have mismatched entries.")