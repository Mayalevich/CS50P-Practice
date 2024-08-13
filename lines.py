import sys
import os

if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

filename = sys.argv[1]
if not filename.endswith('.py'):
        sys.exit("Not a Python file")
if not os.path.isfile(filename):
        sys.exit("File does not exist")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

count = 0
for line in lines:
    stripped_line = line.lstrip()
    if stripped_line != "" and not stripped_line.startswith('#'):
        count += 1
print(count)
