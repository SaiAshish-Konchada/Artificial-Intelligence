#importing the required library 
import cv2

#Loading the image
image = cv2.imread("Sample Image.jpg")
#convert color image into grayscale
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#Displaying the original image
cv2.imshow("Original Image", image)
#Displaying the grayscale image
cv2.imshow("Grayscale Image", gray_image)
#Saving the grayscale image
cv2.imwrite("Grayscale Image.jpg", gray_image)
# wait and displaying the window until a key is pressed
cv2.waitKey(0)
#destroy all windows
cv2.destroyAllWindows()
