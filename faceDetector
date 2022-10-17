import cv2
import numpy as np
from PIL import Image
import pickle
import sqlite3

faceDetect=cv2.CascadeClassifier('xml/haarcascade_frontalface_alt.xml');
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create();
#rec.read("recognizer\\trainningData.yml")
id=0


fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255,51,51)


def getProfile(id):
    peopleSql=sqlite3.connect("them database ho tui nha")
    cursor=peopleSql.execute("SELECT * FROM DATABASE WHERE ID="+str(id))
    profile=None
    for row in cursor:
        profile=row
    peopleSql.close()
    return profile

while(True):

    img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if(profile!=None):
            #cv2.PutText(cv2.fromarray(img),str(id),(x+y+h),font,(0,0,255),2);
            cv2.putText(img, "Name: " + str(profile[1]), (x,y+h+30), fontface, fontscale, fontcolor ,2)
            cv2.putText(img, "Age: " + str(profile[2]), (x,y+h+60), fontface, fontscale, fontcolor ,2)
            cv2.putText(img, "Gender: " + str(profile[3]), (x,y+h+90), fontface, fontscale, fontcolor ,2)
        
        cv2.imshow('Face',img) 
    if cv2.waitKey(0): break;
cam.release()
cv2.destroyAllWindows()
