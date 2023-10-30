import json


IN_PATH = "berkeley_posts_2023-09(1).json"
OUT_PATH = "berkeley_posts_2023-09(final).json"

all_data = []
with open(IN_PATH, 'r') as json_file:
    for line in json_file:
        all_data.append(json.loads(line))

# Load existing data from the file (if it exists)
try:
    with open(OUT_PATH, 'r') as json_file:
        existing_data = json.load(json_file)
except FileNotFoundError:
    existing_data = []

# Append new data to the existing data list
existing_data.extend(all_data)

# Write the updated data (existing + new) back to the file
with open(OUT_PATH, 'w') as json_file:
    json.dump(existing_data, json_file)