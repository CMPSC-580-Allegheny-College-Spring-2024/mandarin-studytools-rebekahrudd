"""To test functions."""


# 1. read in an image
# 2. crop it (or could convert to png)
# to crop use background fader then dtermine
# print with dimensions and then ask the user to decide where to crop
# 3. save the edited image
# 4. extract text from the edited image


# next folder evaluate the text and then create the flashcards


# sources
# open a picture using open cv: https://www.geeksforgeeks.org/reading-image-opencv-using-python/
# resizing a photo: https://www.geeksforgeeks.org/image-resizing-using-opencv-python/
# 

# 1. read in an image
import cv2
import numpy as np
import matplotlib.pyplot as plt
# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("img1.png", cv2.IMREAD_COLOR)
 
# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
cv2.imshow("image", img)

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

img = cv2.imread(image_path, cv2.IMREAD_COLOR)
functions.resize_image(img)
functions.open_photo(img)
# left, right, top, bottom from the user's input
functions.crop(img, left, right, top, bottom)
# ask the user if this is a good crop
functions.close_photo(img)
print("Click any key to close the first image, then your cropped image will show.")
print("Is this a good crop?")
if "yes":
    functions.open_photo(img)
    functions.crop(img, left, right, top, bottom)

# need to figure out how to end this
# let the user check the photo if good then continue

def open_photo(image_loaded) -> None:
    """To open and display a picture on you screen"""
    # name, read image
    # cv2.imshow(image_loaded, img)
    #Displaying image using plt.imshow() method
    plt.imshow(image_loaded)
    #hold the window
    

def resize_image(image_loaded) -> None:
    width, height = image_loaded.size
    # I want the pixels to be bellow 500
    # how to solve for this??
    if x/y / num < 500:
    # if vertical:
        cv2.resize(image_loaded, (x/num, y/num), cv2.INTER_CUBIC)
    
def crop(image_loaded, left, right, top, bottom) -> None:
    cropped_image = image_loaded.crop((left, top, right, bottom))
    cropped_image.show()

def close_photo() -> None:
    """To close the photo with a keystroke."""
    # after user done putting sizes to crop in
    # can close with a key stroke
    plt.waitforbuttonpress()
    plt.close('all')