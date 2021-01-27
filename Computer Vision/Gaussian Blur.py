#importing the required libraries
import cv2

#loading the image
image = cv2.imread("Sample Image.jpg")
#applying the gaussian blur
gaussianBlurImg = cv2.GaussianBlur(image, (21, 21), 0)
#displaying the image
cv2.imshow("Blurred Image", gaussianBlurImg)
# wait and displaying the window until a key is pressed
cv2.waitKey(0)
#destroy all windows
cv2.destroyAllWindows()
