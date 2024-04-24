import csv
import os

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
    # Enter Absolute Path of the input file
    input_file = input("Please enter the location of the input file: ")
    directory, filename = os.path.split(input_file)
    base, ext = os.path.splitext(filename)
    output_file = os.path.join(directory, base + "_Formated" + ext)

    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['First Name', 'Last Name'] + [name for name in reader.fieldnames if name not in ['fullName', 'id', 'tier', 'First Name', 'Last Name']] + [ 'Street','City', 'State', 'Zip']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write the header to the output file
        writer.writeheader()

        rows = []
        # Process each row in the input file
        for row in reader:
            # Skip empty rows
            if not any(row.values()):
                continue

            full_name = row['fullName']
            first_name, last_name = split_name(full_name)

            # Add separated names to the row
            row['First Name'] = first_name
            row['Last Name'] = last_name

            # Remove the original full name from the row
            del row['fullName']
            del row['id']
            del row['tier']

            # Add the row to the list
            rows.append(row)

        # Sort the rows by 'Last Name' in ascending order
        rows = sorted(rows, key=lambda row: row['Last Name'])

        # Write the sorted rows to the output file
        for row in rows:
            writer.writerow(row)

    print("Names separated and sorted successfully. Output saved to", output_file)

if __name__ == "__main__":
    main()
