#importing the required library 
import cv2

#Loading the image
image = cv2.imread("Sample Image.jpg")
#Saving a copy of the image
cv2.imwrite("Sample Image Copy.jpg", image)
#Displaying the sample image
cv2.imshow("Sample Image", image)
# wait and displaying the window until a key is pressed
cv2.waitKey(0)
#destroy all windows
cv2.destroyAllWindows()
