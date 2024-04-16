import csv

def split_name(full_name):
    # Split the full name into first name and last name
    names = full_name.split()
    if names:
        first_name = names[0]
        last_name = ' '.join(names[1:])
    else:
        first_name = ''
        last_name = ''
    return first_name, last_name

def main():
    input_file = 'input.csv'
    output_file = 'output.csv'

    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['First Name', 'Last Name']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write the header to the output file
        writer.writeheader()

        # Process each row in the input file
        for row in reader:
            full_name = row['fullName']
            first_name, last_name = split_name(full_name)

            # Add separated names to the row
            row['First Name'] = first_name
            row['Last Name'] = last_name

            # Write the row to the output file
            writer.writerow(row)

    print("Names separated successfully. Output saved to", output_file)

if __name__ == "__main__":
    main()
