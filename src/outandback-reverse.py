import csv

# Define input and output file names
input_file = 'input.txt'
output_file = 'output_combined.txt'

# Read the input file with tabs as delimiter
with open(input_file, 'r', newline='') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    rows = list(reader)  # Convert to a list to enable processing

# Reverse the order of the rows and combine with the original list
reversed_rows = rows[::-1]
combined_rows = rows + reversed_rows

# Write the combined rows to the output file
with open(output_file, 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames, delimiter='\t')
    writer.writeheader()  
    writer.writerows(combined_rows) 

print(f"Combined original and reversed records written to {output_file}")