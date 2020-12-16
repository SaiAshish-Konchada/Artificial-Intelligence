import cv2
#import os
#dataset = "dataset"
#name = "champ"

#path = os.path.join(dataset,name)
#if not os.path.isdir(path):
#    os.mkdir(path)

#(width,height) = (130,100)
alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)

#count = 1
while True:
#    print(count)
    _,img = cam.read()
    text="face not detected"
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        text="Face Detected"
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
 #       faceOnly = grayImg[y:y+h,x:x+w]
 #       resizeImg = cv2.resize(faceOnly,(width,height))
 #       cv2.imwrite("%s/%s.jpg" %(path,count),resizeImg)
 #       count+=1
    print(text)
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break
print("Image Captured successfully")
cam.release()
cv2.destroyAllWindows()