"""Define functions necessary to read in an image."""


import cv2
import matplotlib.pyplot as plt
 
def open_photo(image_loaded) -> None:
    """To open and display a picture on you screen"""
    # name, read image
    # cv2.imshow(image_loaded, img)
    #Displaying image using plt.imshow() method
    plt.imshow(image_loaded)
    #hold the window

def resize_image(image_loaded) -> None:
    """Resize and image."""
    width, height = image_loaded.size()
    # I want the pixels to be bellow 500
    # how to solve for this??
    num = 4
    if width / num < 500:
    # if vertical:
        cv2.resize(image_loaded, (width/num, height/num), cv2.INTER_CUBIC)
    print("change resize function.")

def crop(image_loaded, left, right, top, bottom) -> None:
    """Crop an image."""
    cropped_image = image_loaded.crop((left, top, right, bottom))
    cropped_image.show()

def close_photo() -> None:
    """To close the photo with a keystroke."""
    # after user done putting sizes to crop in
    # can close with a key stroke
    plt.waitforbuttonpress()
    plt.close('all')