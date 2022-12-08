import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import matplotlib.image as mpimg
import PIL
from PIL import Image
from PIL.Image import *
from numpy import asarray

image = open('test5.jpg')
image = np.array(image)
print(image.size)

def convert_grayscale(image):
    #image.size = (width, height) 
      # Create new Image and a Pixel Map
    new = PIL.Image.new(mode="RGB", size=(200, 200))
    #width = 200
    #height = 200
  #new = create_image(width, height)
    pixels = new.load()

  # Transform to grayscale
    for i in range(0, 200):
        for j in range(0, 200):
      # Get Pixel
            pixel = new.getpixel(i, j)

      # Get R, G, B values (This are int from 0 to 255)
            red =   pixel[0]
            green = pixel[1]
            blue =  pixel[2]

      # Transform to grayscale
            gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

      # Set Pixel in new image
            pixels[i, j] = (int(gray), int(gray), int(gray))

    # Return new image
            return new

convert_grayscale('test5.jpg')

# def filtre_rouge(img_orig):
    
#     im = np.copy(img_orig) 
#     im = np.array(im)
#     print(im)
#     for i in range(im.shape[0]):
#         for j in range(im.shape[1]):
#             for k in range(im.shape[2]):
#                     # r, v, b = im[i, j, k]
#                     # im[i, j, k] = (r, 0, 0)
#                     im[i, j, k] = im[i, 0, 0]
#     return im
# filtre_rouge(image)
# image.show()

# # def filtre_bleu(img_orig):
# #     im = np.copy(img_orig) 
# #     for i in range(im.shape[0]):
# #         for j in range(im.shape[1]):
# #             r, v, b = im[i, j]
# #             im[i, j] = (0, 0, b)
# #     return im

# # filtre_bleu(image)
# # image.show()