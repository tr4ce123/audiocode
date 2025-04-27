import csv

input_file = "./model/training_data.csv"
output_file = "./model/training_data_fixed.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

    for row in reader:
        # Only keep the first two columns and quote them
        if len(row) >= 2:
            writer.writerow([row[0].strip(), row[1].strip()])