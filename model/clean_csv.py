import csv

input_file = "./model/training_data.csv"
output_file = "./model/training_data_fixed.csv"

fixed_rows = []

def clean_field(text):
    if text is None:
        return ""
    text = text.strip()
    text = text.replace('"', "'")
    return text

with open(input_file, "r", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    for row in reader:
        # Skip empty lines
        if not row or all(cell.strip() == "" for cell in row):
            continue

        if len(row) != 2:
            print(f"⚠️ Skipping malformed row: {row}")
            continue
        
        input_text = clean_field(row[0])
        target_text = clean_field(row[1])

        if target_text.endswith("("):
            target_text += ")"
        if target_text.count('(') > target_text.count(')'):
            target_text += ")"

        fixed_rows.append([input_text, target_text])

with open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
    writer.writerow(["input_text", "target_text"])  # header
    writer.writerows(fixed_rows)

print(f"✅ Cleaned and saved {len(fixed_rows)} examples into {output_file}")
