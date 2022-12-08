# pip install Pillow

import matplotlib as plt
from matplotlib import pyplot
import matplotlib.image as mpimg
import numpy as np

#print('Pillow Version:', PIL.__version__)

from PIL import Image
image = Image.open('logo_42AI.png')
# class ImageProcessor
# - load : path PNG, array RGB divmoddisplay array 
print(image.format)
print(image.size)
print(image.mode)
image.show()


# ----------- OR ----------ne Foe pas ----------------------
# from matplotlib import image
# from matplotlib import pyplot

# import matplotlib.pyplot as plt
# import matplotlib.image as img

# image = img.imread('logo_42AI.png')
# imgplot = plt.imshow(image)
# print(image.dtype)
# print(image.shape)

# pyplot.imshow(image)
# pyplot.show()

# im = cv2.imread('logo_42AI.png')
# im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)

# plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
# plt.show()

#------------------------------------------------------------------

from numpy import asarray

image = Image.open('logo_42AI.png')
data = asarray(image)
print(type(data))
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)
new_image = image.resize((200, 200))
#new_image.save('image_200.jpg')
print(image.size)
print(new_image.size) 

print(data)
div = data / 255
print(div)

#---------------------------------------------------------------------
def filtre_rouge(img_orig):
    im = np.copy(img_orig) 
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]
            im[i, j] = (r, 0,0)
    return im

filtre_rouge(image)
image.show()