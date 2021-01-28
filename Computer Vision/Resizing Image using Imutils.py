#importing the required libraries
import cv2
import imutils

#loading an image
img = cv2.imread("Sample Image.jpg")
#resizing an image
resizeImg = imutils.resize(img, width=20)
#saving the resized image
cv2.imwrite("Resized Image.jpg", resizeImg)
