#importing the required library
import cv2

#initialise the primary camera for video capture
vs = cv2.VideoCapture(0)
while True:
    #obtain the frame from the camera
    _,img = vs.read()
    #display the video stream
    cv2.imshow("VideoStream", img)
    #masking the values and obtaining the key
    key = cv2.waitKey(1) & 0xFF
    #terminate the loop if user presses 'q'
    if key == ord("q"):
        break
#release the camera and stop streaming
vs.release()
#destroy all windows
cv2.destroyAllWindows()
