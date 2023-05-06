import csv

# Open the first file and store the data in a list
with open('file1.csv', newline='') as file1:
    reader1 = csv.reader(file1)
    data1 = list(reader1)

# Open the second file and store the data in a list
with open('file2.csv', newline='') as file2:
    reader2 = csv.reader(file2)
    data2 = list(reader2)

# Compare the two lists and find the differences
differences = []
for row in data1:
    if row not in data2:
        differences.append(('file1', row))
for row in data2:
    if row not in data1:
        differences.append(('file2', row))

# Output the differences
if len(differences) == 0:
    print("The two lists are identical")
else:
    print("The following rows are different:")
    for diff in differences:
        print(f"{diff[0]}: {diff[1]}")
