#!/usr/bin/env python3
import csv
import json

data = {}

input_file = "concerts_rennes"
with open(input_file+".csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

print(json.dumps(data, indent=2))

with open(input_file+'.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile)

print(f"Json data has been written to {input_file}.json")