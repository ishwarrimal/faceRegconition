import cv2

import numpy

import sys

image="face/database/image.png"

image1=cv2.imread(image)

#image=cv2.imread("img.jpg")

breadth = 150.0 / image1.shape[1]

dimension = (125, int(image1.shape[0] * breadth))
 
# perform the actual resizing of the image and show it

resized = cv2.resize(image1, dimension, interpolation = cv2.INTER_AREA)

#save the image

cv2.imwrite("face/database/image.png",resized)

cv2.imshow("image","face/database/image.png")

cv2.waitKey(0)
