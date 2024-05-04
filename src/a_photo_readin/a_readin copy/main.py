"""Run the picture evaluation."""

# import typer
# from rich.console import Console
import functions

import cv2

# create a Typer object to support the command-line interface
# cli = typer.Typer()

# create a console for display of rich text
# console = Console()

# Add comments to explain the steps in the main function
# @cli.command()
# def main(image_name: str):
#     """Edit a picture"""
    # To read image from disk, we use
    # cv2.imread function, in below method,

image_name = input("Enter the image name: ")
img = cv2.imread(image_name)

# functions.resize_image(img)

# functions.open_photo(img)

# left, right, top, bottom from the user's input
print("Reference the photo to get numbers on where you want the image cropped.")
left = int(input("Enter the left amount you want cropped: "))
right = int(input("Enter the right amount you want cropped: "))
top = int(input("Enter the top amount you want cropped: "))
bottom = int(input("Enter the bottom amount you want cropped: "))
# functions.pic_crop(image_name, left, top, right, bottom)
functions.fake_crop(image_name)

# ask the user if this is a good crop
functions.close_photo(img)
# print("Click any key to close the first image, then your cropped image will show.")
response = input(f"""Is this a good crop? Enter "yes" or nothing """)
if response == "yes":
    print("yay!")
    functions.open_photo(img)
    # functions.crop(img, left, top, right, bottom)
# functions.pic_crop("img1.png", 10, 10, 10, 10)