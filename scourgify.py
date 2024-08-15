import sys
import csv

if len(sys.argv) != 3:
    sys.exit(1)

input = sys.argv[1]
output = sys.argv[2]

try:
    input_file = open(input, 'r')
except FileNotFoundError:
    sys.exit(1)

read = csv.reader(input_file)

output_file = open(output, 'w', newline='')
write = csv.writer(output_file)

write.writerow(['first', 'last', 'house'])
next(read)

for row in read:
    name, house = row
    last, first = name.split(", ")
    write.writerow([first, last, house])
