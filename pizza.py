import sys
import os
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    print("Too few or too many command-line arguments")
    sys.exit(1)

filename = sys.argv[1]
if not filename.endswith('.csv'):
    print("Not a CSV file")
    sys.exit(1)

if not os.path.isfile(filename):
    print("File does not exist")
    sys.exit(1)

try:
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        table = [row for row in reader]
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)


if table:
    print(tabulate(table, headers="keys", tablefmt="grid"))
else:
    print("CSV file is empty")
