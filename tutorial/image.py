import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("/home/carlitos/Downloads/dog.jpg"))

if img is None:
    sys.exit("Couldn't read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("/home/carlitos/Downloads/dog.png", img)