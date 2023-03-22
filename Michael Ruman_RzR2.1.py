from PIL import Image
import numpy as np


path = "data/lenna.png"
img = Image.open(path).transpose(Image.FLIP_LEFT_RIGHT)
pixels = img.load()

for y in range(img.height):
    for x in range(img.width):
        pixels[x, y] = 255 - pixels[x, y][0], 255 - pixels[x, y][1], 255 - pixels[x, y][2]

img.show()
