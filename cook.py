# Read vegetables.csv
import csv
import json

with open('vegetables.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Write vegetables.json
with open('vegetables.json', 'w') as f:
    json.dump(rows, f, indent=2)