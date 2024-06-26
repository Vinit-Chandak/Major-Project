import json
import os

correct = 0
wrong = 0

# Get the directory containing the JSON files (modify if needed)
directory = '' 

# Iterate through the files in the directory
for filename in os.listdir():
    if filename.startswith("figureqa_analyzed_block") and filename.endswith(".json"):
        with open(filename, 'r') as file:
            data = json.load(file)

            # Compare 'answer' and 'gemini_answer' in each entry
            for entry in data:
                if entry['answer'] == entry['gemini_answer']:
                    correct += 1
                else:
                    wrong += 1

print("Total Questions:", correct + wrong)
print("Total Correct Gemini Answers:", correct)
print("Total Wrong Gemini Answers:", wrong)
print("Accuracy:", correct / (correct + wrong) * 100, "%")
