import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# print(image_folder, output_folder)

# check if "Pokedex_png/" this file exists or not, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex
for filename in os.listdir(image_folder):
    # opening the files
    img = Image.open(f"{image_folder}{filename}")

    # deleting the jpeg extension
    without_extension = os.path.splitext(filename)[0]
    # print(without_extension) comment out the line below and print this instead

    # converting image files (without extension) to png
    # saving them in the Pokedex_png folder
    img.save(f"{output_folder}{without_extension}.png", 'png')  # giving PNG extension to the Pokedex_png files
