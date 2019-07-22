import numpy as np
import cv2

leye=cv2.CascadeClassifier('data/haarcascade_lefteye_2splits.xml')
reye=cv2.CascadeClassifier('data/haarcascade_righteye_2splits.xml')

cap = cv2.VideoCapture(0)
print(leye)
print("")
print(reye)

while(True):
    
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ry = reye.detectMultiScale(gray,1.3,10)
    ly = leye.detectMultiScale(gray,1.3,10)
    for (x,y,w,h) in ly:
        endx=x+w
        endy=y+h
        ex=x+int(w/1.9)
        ey=y+int(h/1.5)
        cv2.circle(frame,(ex,ey),int((endx+endy)/5120),(0,0,127),15)
    for (x,y,w,h) in ry:
        endx=x+w
        endy=y+h
        ex=x+int(w/1.9)
        ey=y+int(h/1.5)
        cv2.circle(frame,(ex,ey),int((endx+endy)/5120),(127,0,0),15)

    
    cv2.imshow('eyeTrack',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
