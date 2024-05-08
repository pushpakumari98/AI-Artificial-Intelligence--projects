import cv2
       
   
alg="haarcascade_frontalface_alt.xml" #Loading harcascade face Algorithm
haar_cascade=cv2.CascadeClassifier(alg) #load the algorithm inside computer vision in the variable
cam=cv2.VideoCapture(2) #initialising camera



while True:
    _,img=cam.read() #reading frame from camera
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert color image into grayscale
    face=haar_cascade.detectMultiScale(grayImg,1.3,4) #to get coordinate of face
    for (x,y,w,h) in face:
          cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)#drawing rectangle on the face algorithm
        
    cv2.imshow("FaceDetection",img) #display the output frame
    key=cv2.waitKey(10)
    if key == 27: #27 is for pressing an escape(Esc) button
        break
cam.release()
cv2.destroyAllWindows()

