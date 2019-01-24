# lab16-image-manipulation_v1.py

from PIL import Image

img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

# img = img.convert("L")

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y =  (r * 0.299) + (g * 0.587) + (b * 0.114)

        pixels[i, j] = (int(y), int(y), int(y))

print(pixels[i,j])
print(r)

img.show()