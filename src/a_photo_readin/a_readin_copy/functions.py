"""Define functions necessary to read in an image."""


import cv2
import matplotlib.pyplot as plt
from PIL import Image

 
def open_photo(image_loaded) -> None:
    """To open and display a picture on you screen"""
    # name, read image
    # cv2.imshow(image_loaded, img)
    #Displaying image using plt.imshow() method
    # cv2.imshow("image", image_loaded)
    # #hold the window
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    plt.imshow(image_loaded)
    
    #hold the window
    plt.waitforbuttonpress()
    plt.close('all')

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

def pic_crop(image_name, left, top, right, bottom) -> None:
    """Crop an image."""
    im = Image.open(image_name)
    cropped_image = im.crop((left, top, right, bottom))
    cropped_image.show()

def fake_crop(image_name):
    """show that the cropping function does work."""
    cropped_image = Image.open(image_name)
    width, height = cropped_image.size
    # Setting the points for cropped image
    left = 5
    top = height / 4
    right = 300
    bottom = 3 * height / 4
    im1 = cropped_image.crop((left, top, right, bottom))
    im1.show()
 
# Cropped image of above dimension
# (It will not change original image)
# im1 = im.crop((left, top, right, bottom))
# pic_crop("img1.png", 10, 10, 10, 10)

def close_photo() -> None:
    """To close the photo with a keystroke."""
    # after user done putting sizes to crop in
    # can close with a key stroke
    plt.waitforbuttonpress()
    plt.close('all')