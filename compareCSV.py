#!/usr/bin/env python3

import csv

# Open the first file and store the data in a list
with open('file1.csv', newline='') as file1:
    reader1 = csv.reader(file1)
    data1 = [row for row in reader1 if any(row)] # Only includes non-empty rows

# Open the second file and store the data in a list
with open('file2.csv', newline='') as file2:
    reader2 = csv.reader(file2)
    data2 = [row for row in reader2 if any(row)] # Only includes non-empty rows

# Compare the two lists and find the differences
missingFromFile1 = []
missingFromFile2 = []
for row in data1:
    if row not in data2:
        missingFromFile2.append(row)
for row in data2:
    if row not in data1:
        missingFromFile1.append(row)

# Output the differences
# Identical lists
if len(missingFromFile1) == 0 and len(missingFromFile2) == 0:
    print("The two lists are identical")
# Rows missing from File 1, but not File 2
elif len(missingFromFile1) != 0 and len(missingFromFile2) == 0:
    print("No rows missing from File 2")
    print("")
    print("The following rows are missing from File 1:")
    for diff in missingFromFile1:
        print(f"{diff[0]}")
# Rows missing from File 2, but not File 1
elif len(missingFromFile1) == 0 and len(missingFromFile2) != 0:
    print("No rows missing from File 1")
    print("")
    print("The following rows are missing from File 2:")
    for diff in missingFromFile2:
        print(f"{diff[0]}")
# Rows missing from both files
else:
    print("The following rows are missing from File 1:")
    for diff in missingFromFile1:
        print(f"{diff[0]}")
    print("")
    print("The following rows are missing from File 2:")
    for diff in missingFromFile2:
        print(f"{diff[0]}")