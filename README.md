# Readme

## Introduction

This Python script is designed to compare two CSV files and find the differences between them. It can be used to check whether two CSV files contain identical data or whether one file has additional or missing rows compared to the other file.

## Requirements

This script requires Python 3.x and the `csv` module, which is included in the standard library.

## How to use

1. Save the script in a file with a `.py` extension.
2. Put the two CSV files you want to compare in the same directory as the script.
3. Rename the files to `file1.csv` and `file2.csv`.
4. Open a terminal or command prompt and navigate to the directory where the script and CSV files are located.
5. Run the script with the following command:

```sh
python script_name.py
```

Make sure to replace `script_name.py` with the actual name of the script file.

## Output

The script will output the following depending on the differences found:

- If the two lists are identical, the script will output "The two lists are identical".
- If there are rows missing from `file1.csv`, the script will output "No rows missing from File 2", followed by the list of missing rows from `file1.csv`.
- If there are rows missing from `file2.csv`, the script will output "No rows missing from File 1", followed by the list of missing rows from `file2.csv`.
- If there are rows missing from both files, the script will output the list of missing rows from `file1.csv`, followed by a blank line, followed by the list of missing rows from `file2.csv`.

## Limitations

- The script assumes that the two CSV files have the same format (i.e., the same number of columns and the same column names).
- The script only compares the rows of the two CSV files. If there are differences in the column values of the same row, the script will not detect them.