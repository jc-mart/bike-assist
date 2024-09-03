import numpy as np
import cv2 as cv

# Black image
img = np.zeros((512, 512, 3), np.uint8)

# Object, start, end, color, thickness
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord('q'):
    exit()