import numpy as np
import requests
from io import BytesIO
from PIL import Image
from cairosvg import svg2png
import cv2
import os

# svg_url = 'https://logincdn.msauth.net/16.000.28611.4/content/images/microsoft_logo_ee5c8d9fb6248c938fd0dc19370e90bd.svg'

# svg_data = requests.get(svg_url).content

# png = svg2png(bytestring=svg_data)

open_svg = open("11904.svg")

open_svg.close
os.popen("inkscape -z -e testImage.png -w 1024 -h 1024 11904.svg")

pil_img = Image.open(BytesIO(open_svg)).convert('RGBA')
# pil_img.save('output/pil.png')

# cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGBA2BGRA)
# cv2.imwrite('cv.png', cv_img)