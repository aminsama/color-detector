import cv2
import numpy as np

image = cv2.imread('d:/test.PNG')

color_boundaries = {
    "red":    ([0,   0,   255], [127, 0,   255]),
    "blue":   ([255, 0,  0],   [255, 85,  0]),
    "green": ([0,   255, 0], [55,   255, 0]),
    "white":   ([255, 255, 255], [255, 255, 255]),
    "black":   ([0, 0, 0], [0, 0, 0])
}


for color_name, (lower, upper) in color_boundaries.items():
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = np.uint8)
    upper = np.array(upper, dtype = np.uint8)

    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    if mask.any():
        print(f"{color_name}")
