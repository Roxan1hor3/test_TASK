import cv2
import numpy as np
from PIL import Image, ImageDraw


def find_brightest_darkest_spot_v1(img_path):
    """will find the lightest and darkest pixel"""
    img_for_find_brightest_spot = cv2.imread(img_path)
    img_rgb = np.copy(img_for_find_brightest_spot)
    img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(img_rgb)
    img = Image.open(img_path)
    idraw = ImageDraw.Draw(img)
    idraw.rectangle((maxLoc[1] - 50, maxLoc[0] - 50, maxLoc[1] + 50, maxLoc[0] + 50), outline=(255, 0, 0), width=10)
    idraw.rectangle((minLoc[1] - 50, minLoc[0] - 50, minLoc[1] + 50, minLoc[0] + 50), outline=(0, 0, 0), width=10)
    img.save('change.png')
    img.show()


find_brightest_darkest_spot_v1('img.png')


