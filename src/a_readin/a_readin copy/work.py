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
cv2.waitKey(0)
 
# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()

# user input, imagepath
