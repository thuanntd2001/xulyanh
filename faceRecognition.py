import face_recognition
import cv2
import dlib



image_path='img/1.jpg'

face_detector=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

img=cv2.imread(image_path)

img_gray=cv2.cvtColor(src=img,code=cv2.COLOR_BGR2GRAY)

while True:
    count=0
    faces=face_detector.detectMultiScale(img_gray,1.3,5)

    for(x,y,w,h) in faces:
        img_face=cv2.resize(img[y+3:y+h-3,x+3:x+w-3],(70,70))
        cv2.imwrite('img/people_{}.jpg'.format(count),img_face)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        count +=1


    cv2.imshow('Face recongition',img)
    if cv2.waitKey(delay=0): break
    cv2.destroyAllWindows()
