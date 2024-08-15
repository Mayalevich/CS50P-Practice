import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

input_ext = os.path.splitext(input_filename)[1].lower()
output_ext = os.path.splitext(output_filename)[1].lower()

if input_ext != '.jpg' and input_ext != '.jpeg' and input_ext != '.png':
    sys.exit(1)
if output_ext != '.jpg' and output_ext != '.jpeg' and output_ext != '.png':
    sys.exit(1)
if input_ext != output_ext:
    sys.exit(1)
if not os.path.isfile(input_filename):
    sys.exit(1)

try:
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit(1)

try:
    photo = Image.open(input_filename)
except FileNotFoundError:
    sys.exit(1)

shirt_size = shirt.size
photo = ImageOps.fit(photo, shirt_size)
photo.paste(shirt, shirt)
photo.save(output_filename)

sys.exit(0)

