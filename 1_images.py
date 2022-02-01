from PIL import Image, ImageFilter

# opening a image file
img = Image.open(r"E:\Python Zero to Mastery Course\17. Scripting with Python\PokeDex\bulbasaur.jpg")
pikachu = Image.open(r"E:\Python Zero to Mastery Course\17. Scripting with Python\PokeDex\pikachu.jpg")

# some applications
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))

# blurring the image
filtered_bulbasaur = img.filter(ImageFilter.BLUR)
filtered_bulbasaur.save("blurbasaur.png", 'png')
# (to save: image file name(have to add extension in this too to run in python editor), extension)

# sharpening the image
filtered_bulbasaur = img.filter(ImageFilter.SHARPEN)
filtered_bulbasaur.save("sharpasaur.png", 'png')

# filtered Pokedex_png are converted into png cause png supports image filters.
# you might get an error if you actually keep it as a jpeg

filtered_bulbasaur = img.convert('L')  # converts to grayscale
rotated_bulbasaur = filtered_bulbasaur.rotate(180)  # rotates the image (180 is the angle)
rotated_bulbasaur.save("greybasaur.png", 'png')
# rotated_bulbasaur.show(): shows/opens up the image

filtered_pikachu = pikachu.convert('L')
resized_pikachu = filtered_pikachu.resize((300, 300))  # to resize, we have to use a tuple inside the brackets
resized_pikachu.save("resized pikachu.png", 'png')

# crop
region = (100, 100, 400, 400)
# The region is defined by a 4-tuple, where coordinates are (left, upper, right, lower)
cropped_pikachu = filtered_pikachu.crop(region)
cropped_pikachu.save("cropped_pikachu.png", 'png')
