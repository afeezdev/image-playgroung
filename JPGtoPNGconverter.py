import sys
import os
from PIL import Image

# grab first and second argument
# check if new/ exists, if not create it
# Loop through Pokedex,
# convert images to png
# save them to the new folder

image_folder = sys.argv[1]
output_folder = sys.argv[2]


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'{output_folder}{clean_name[0]}.png', 'png')
    print('all done!')


# Run in terminal with "python3 JPGtoPNGconverter.py Pokedex/ new/ "