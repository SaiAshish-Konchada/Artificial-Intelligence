#Importing the required libraries
import urllib.request #for handling URLs
import cv2 #for computer vision and image processing 
import numpy as np #for mathematical operations on arrays
import imutils #for basic image processing function

#Replace the IPv4 address obtained from IPWebcam below
url='http://192.168.1.6:8080/shot.jpg'

while True:
    imgPath = urllib.request.urlopen(url) #opens the requested url
    imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8) #obtaining data of the image captured from the phone
    img = cv2.imdecode(imgNp, -1) #decode and convert the data obtained into an image
    img = imutils.resize(img, width=450) #resize the frame to 450px wide
    cv2.imshow("CameraFeed",img) #display the camera feed
    #stop streaming when user presses 'q' on keyboard
    if ord('q') ==  cv2.waitKey(1):
        exit(0)
