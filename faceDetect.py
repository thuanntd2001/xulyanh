
from itertools import count
import cv2


def faceDetect(img):
    pad =30
    size = 100
    deltaY=10
    face_detector=cv2.CascadeClassifier('xml/haarcascade_frontalface_alt.xml')
    height, width, channels = img.shape
    img_gray=cv2.cvtColor(src=img,code=cv2.COLOR_BGR2GRAY)

    count=0
    faces=face_detector.detectMultiScale(img_gray,1.3,1)

    for(x,y,w,h) in faces:
        if x-pad >0:
            x-=pad
        else: x=0

        if y-pad >0:
            y-=pad+deltaY
        else: y=0

        if h+2*pad <height:
            h+=2*pad
        else: h=height

        if w+2*pad <width:
            w+=2*pad
        else: w=width
    
        img_face=cv2.resize(img[y+3:y+h-3,x+3:x+w-3],(size,size))
        cv2.imwrite('output/faceDetect/people_{}.jpg'.format(count),img_face)
        count +=1
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return img

