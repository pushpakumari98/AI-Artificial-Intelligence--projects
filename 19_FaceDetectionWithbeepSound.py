import cv2
import time
import pygame
from pygame.locals import *

pygame.init()

pygame.mixer.init()
beep_sound = pygame.mixer.Sound("beep-01a.wav")

alg="haarcascade_frontalface_default.xml"

    #load the pretrained Haar cascade classifier for face detection
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


    #open the primary camera
cam=cv2.VideoCapture(2)
time.sleep(1)

while True:
    _,img=cam.read()
    text="No person detected"
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(grayimg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="Person Detected"
        beep_sound.play()
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("FaceDetection", img)        
    key = cv2.waitKey(10)
    if key == ord("s"):
        break
cam.release()
cv2.destroyAllWindows()


        
