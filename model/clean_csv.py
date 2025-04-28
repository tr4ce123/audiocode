import csv
import re

input_file = "./model/training_data.csv"
output_file = "./model/training_data_fixed.csv"

fixed_rows = []

# Utility: Clean and wrap fields properly
def clean_field(text):
    if text is None:
        return ""
    text = text.strip()
    text = text.replace('"', "'")
    return text

with open(input_file, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

for line in lines:
    # Skip empty lines
    if not line.strip():
        continue

    parts = line.strip().split(",", 1)

    if len(parts) != 2:
        print(f"Warning: Skipping malformed line: {line}")
        continue

    input_text = clean_field(parts[0])
    target_text = clean_field(parts[1])

    if target_text.endswith("("):
        target_text += ")"
    if target_text.count('(') > target_text.count(')'):
        target_text += ")"

    fixed_rows.append([input_text, target_text])

with open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
    writer.writerow(["input_text", "target_text"])  # header
    writer.writerows(fixed_rows)

print(f"✅ Fixed and saved {len(fixed_rows)} examples into {output_file}")
