from io import BytesIO
import numpy as np
import requests
from PIL import Image
from cairosvg import svg2png
import cv2

# a big part which I haven't looked into at all
# will be looking into user interface and interacting with the svg
# svg_url = 'file:///home/student/Downloads/11904.svg'

# # Get svg data
# svg_data = requests.get(svg_url).content

# # Convert from svg to png
png = svg2png(bytestring="11904.svg")

# Open png in PIL
pil_img = Image.open(BytesIO(png))
pil_img.show()  # This looks good

# Convert to opencv
cv_img = np.array(pil_img.convert('RGB'))[:, :, ::-1].copy()  # Taken from https://stackoverflow.com/questions/14134892/convert-image-from-pil-to-opencv-format
cv2.imshow('cv_img', cv_img)  # This does not look right
cv2.waitKey(0)