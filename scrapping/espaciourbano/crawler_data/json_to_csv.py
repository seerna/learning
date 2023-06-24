import csv
import json

# Load JSON data from file
with open('copy_main_data.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the keys from the JSON data
keys = list(data[0].keys())

# Specify the output CSV file path
csv_file = 'output.csv'

# Write the JSON data to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=keys, quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    writer.writerows(data)