#importing the required libraries
import cv2

#loading the image
img = cv2.imread("Sample Image.jpg")
#converting image into grayscale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#applying threshold to the grayscale image
thresImg = cv2.threshold(grayImg, 200, 255, cv2.THRESH_BINARY)[1]
#saving the threshold image
cv2.imwrite("Threshold Image.jpg", thresImg)

