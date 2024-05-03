"""Run the picture evaluation."""

import typer
from rich.console import Console
from a_readin import functions

import cv2

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()

# Add comments to explain the steps in the main function
@cli.command()
def main(image_name: str):
    """Edit a picture"""
    # To read image from disk, we use
    # cv2.imread function, in below method,
    img = cv2.imread(image_name, cv2.IMREAD_COLOR)
    functions.resize_image(img)
    functions.open_photo(img)
    # left, right, top, bottom from the user's input
    print("Reference the photo to get numbers on where you want the image cropped.")
    left = input("Enter the left limit you want: ")
    right = input("Enter the right limit you want: ")
    top = input("Enter the top limit you want: ")
    bottom = input("Enter the bottom limit you want: ")
    functions.crop(img, left, right, top, bottom)
    # ask the user if this is a good crop
    functions.close_photo(img)
    print("Click any key to close the first image, then your cropped image will show.")
    response = input(f"""Is this a good crop? Enter "yes" or nothing""")
    if response == "yes":
        functions.open_photo(img)
        functions.crop(img, left, right, top, bottom)