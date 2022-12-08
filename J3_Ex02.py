import numpy as np
from PIL import Image

#class named ScrapBooker
 
# ---------------------crop---------------def crop(self, array, dim, position=(0,0)):------------------- 
# Opens a image in RGB mode
im = Image.open(r"logo_42AI.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 5
top = height / 4
right = 164
bottom = 3 * height / 4
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
 
# Shows the image in image viewer
im1.show()
im1.save('test1.jpg')

#  ------------------- thin ----------------------------------
# pip install itk

# import itk
# import argparse

# parser = argparse.ArgumentParser(description="Thin Image.")
# parser.add_argument("input_image", nargs="?")
# args = parser.parse_args()

# PixelType = itk.UC
# Dimension = 2
# ImageType = itk.Image[PixelType, Dimension]

# if args.input_image:
#     image = itk.imread(args.input_image)

# else:
#     # Create an image
#     start = itk.Index[Dimension]()
#     start.Fill(0)

#     size = itk.Size[Dimension]()
#     size.Fill(100)

#     region = itk.ImageRegion[Dimension]()
#     region.SetIndex(start)
#     region.SetSize(size)

#     image = ImageType.New(Regions=region)
#     image.Allocate()
#     image.FillBuffer(0)

#     # Draw a 5 pixel wide line
#     image[50:55, 20:80] = 255

#     # Write Image
#     itk.imwrite(image, "Input.png")

# image = itk.binary_thinning_image_filter(image)

# # Rescale the image so that it can be seen (the output is 0 and 1, we want 0 and 255)
# image = itk.rescale_intensity_image_filter(image, output_minimum=0, output_maximum=255)

# # Write Image
# itk.imwrite(image, "logo_422AI.png")
# #image.show()
# #image.save('test2.jpg')

# ---------------- juxtapose ---------------------------------------
import sys
from PIL import Image

images = [Image.open(x) for x in ['test1.jpg', 'test2.jpg', 'test4.jpg']]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('test.jpg')

# -------------------------- mosaic  ------------------ne Foe pas----
def load_image(source : str) -> np.ndarray:
    
    #with image rgb data
    
    with Image.open(source) as im:
        im_arr = np.asarray(im)
    return im_arr
im_arr = load_image('test4.jpg')

mos_template = im_arr[::10,::10]

images = []

# for file in glob.glob('../Images/Mosaic-Images/*'):
#     im = load_image(file)
#     images.append(im)
# # The images then go through resizing 
# images_array = np.asarray(images)
# images_array.shape
# OUT: (1000, 40, 40, 3)


image_values = np.apply_over_axes(np.mean, im_arr, [1,2])
#image_values = np.apply_over_axes(np.mean, im_arr, [1,2]).reshape(len(images), (len(images) /3))

from scipy import spatial
tree = spatial.KDTree(image_values)


image_idx = np.zeros(target_res, dtype=np.uint32)
for i in range(target_res[0]):
    for j in range(target_res[1]):
        template = mos_template[i, j]
        match = tree.query(template, k=40)
        pick = random.randint(0, 39)
        image_idx[i, j] = match[1][pick]


canvas = Image.new('RGB', (mosaic_size[0]*target_res[0], mosaic_size[1]*target_res[1]))
for i in range(target_res[0]):
    for j in range(target_res[1]):
        arr = images[image_idx[j, i]]
        x, y = i*mosaic_size[0], j*mosaic_size[1]
        im = Image.fromarray(arr)
        canvas.paste(im, (x,y))
canvas




# 
# """
# Crops the image as a rectangle via dim arguments (being the new height
# and width of the image) from the coordinates given by position arguments.
# Args:
# -----
# array: numpy.ndarray
# dim: tuple of 2 integers.
# position: tuple of 2 integers.
# Return:
# -------
# new_arr: the cropped numpy.ndarray.
# None (if combinaison of parameters not compatible).
# Raise:
# ------
# This function should not raise any Exception.
# """
# ... your code ...
# def thin(self, array, n, axis):
# """
# Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
# Args:
# -----
# array: numpy.ndarray.
# n: non null positive integer lower than the number of row/column of the array
# (depending of axis value).
# axis: positive non null integer.
# Return:
# -------
# new_arr: thined numpy.ndarray.
# None (if combinaison of parameters not compatible).
# Raise:
# ------
# This function should not raise any Exception.
# """
# ... your code ...
# def juxtapose(self, array, n, axis):
# """
# Juxtaposes n copies of the image along the specified axis.
# Args:
# -----
# array: numpy.ndarray.
# n: positive non null integer.
# axis: integer of value 0 or 1.
# Return:
# -------
# new_arr: juxtaposed numpy.ndarray.
# None (combinaison of parameters not compatible).
# Raises:
# -------
# This function should not raise any Exception.
# """
# ... your code ...
# def mosaic(self, array, dim):
# """
# Makes a grid with multiple copies of the array. The dim argument specifies
# the number of repetition along each dimensions.
# Args:
# -----
# array: numpy.ndarray.
# dim: tuple of 2 integers.
# Return:
# -------
# new_arr: mosaic numpy.ndarray.
# None (combinaison of parameters not compatible).
# Raises:
# -------
# This function should not raise any Exception.
# """
# ... your code ...