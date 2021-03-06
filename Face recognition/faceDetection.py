import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
cap =cv2.VideoCapture(0)
id=input('Enter user id:')
sno=0
while True:
    ret , img =cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h)in faces:
        sno = sno + 1
        cv2.imwrite('dataSet/User.' + str(id) + '.' + str(sno) + '.jpg', gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes= eye_cascade.detectMultiScale(roi_gray)
        smile=smile_cascade.detectMultiScale(roi_gray)
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh), (0,255,0),2)
        cv2.imshow('img',img)
        k=cv2.waitKey(200) & 0xff
        if sno>30:
            break
cap.release()
cv2.destroyAllWindows()
