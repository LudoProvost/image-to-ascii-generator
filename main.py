import math
import numpy as np
from PIL import Image


def image_to_ascii(image_data, file):
    f = open(file, 'w')

    ramp_pixel_value = np.zeros(image_data.shape)

    grayscale_ramp = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"^`\'. '
    ramp_length = len(grayscale_ramp)

    image_row = image_data.shape[0]
    image_col = image_data.shape[1]

    for row in range(image_row):
        for col in range(image_col):
            ramp_pixel_value[row, col] = math.ceil((ramp_length - 1) * image_data[row, col] / 255)

    line = ""

    for row in range(image_row):
        print(line)
        print("\n")
        f.write(line)
        f.write("\n")
        line = ""
        for col in range(image_col):
            symbol = grayscale_ramp[int(ramp_pixel_value[row, col])]
            line += symbol
            if col % 1 == 0:
                line += " "

#customizable size
size = 128
image_name = 'homer.jpg'

if size is not None:
    image = Image.open('images/' + image_name).convert('L').resize((size, size))
    image.save('grayscale' + image_name)
else:
    image = Image.open('images/' + image_name).convert('L')
    image.save('grayscale' + image_name)

image_data = np.asarray(image)

image_to_ascii(image_data, 'canvas.txt')
