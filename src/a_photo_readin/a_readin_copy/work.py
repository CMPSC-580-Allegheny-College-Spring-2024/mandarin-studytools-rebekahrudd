"""To test functions."""


# 1. read in an image
# 2. crop it (or could convert to png)
# to crop use background fader then determine
# print with dimensions and then ask the user to decide where to crop
# 3. save the edited image
# 4. extract text from the edited image


# next folder evaluate the text and then create the flashcards


# sources
# open a picture using open cv: https://www.geeksforgeeks.org/reading-image-opencv-using-python/
# resizing a photo: https://www.geeksforgeeks.org/image-resizing-using-opencv-python/
# cropping a photo: https://www.geeksforgeeks.org/python-pil-image-crop-method/


# 1. read in an image
import cv2
import numpy as np
import matplotlib.pyplot as plt
 

# look into the bellow functions more

# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
 
# It is for removing/deleting created GUI window from screen
# and memory

# user input, imagepath
# cv2.waitKey(0)
# got this error
# cv2.error: OpenCV(4.9.0) /io/opencv/modules/highgui/src/window.cpp:1272: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvShowImage'

# import cv2
# import matplotlib.pyplot as plt

# # print(cv2.getBuildInformation())
 
# def open_photo(image_loaded) -> None:
#     """To open and display a picture on you screen"""
#     # name, read image
#     # cv2.imshow(image_loaded, img)
#     #Displaying image using plt.imshow() method
#     # cv2.imshow("image", image_loaded)
#     # #hold the window
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
#     plt.imshow(img)
    
#     #hold the window
#     plt.waitforbuttonpress()
#     plt.close('all')


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img=cv2.imread("img1.png")
# #Displaying image using plt.imshow() method
# # plt.imshow(img)
 
# # #hold the window
# # plt.waitforbuttonpress()
# # plt.close('all')



# crop(img, 500, 500, 200, 0)

from PIL import Image
 
# Opens a image in RGB mode

im = Image.open("img1.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 5
top = height / 4
right = 300
bottom = 3 * height / 4
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
 
# Shows the image in image viewer
im1.show()