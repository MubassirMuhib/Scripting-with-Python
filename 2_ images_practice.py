from PIL import Image

astro = Image.open(r"E:\Python Zero to Mastery Course\17. Scripting with Python\Images\astro.jpg")

# using resize
resized_astro = astro.resize((400, 200))
resized_astro.save("resized_astro.png", 'png')
# .resize compresses the image. That's a problem

# using thumbnail
astro.thumbnail((400, 400))  # (.thumbnail modifies the original image)
astro.save("thumbnail_astro.jpg")
print(astro.size)
