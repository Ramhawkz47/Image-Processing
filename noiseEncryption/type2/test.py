import cv2
import numpy as np


#f=input("").split()
img=cv2.imread("blank.jpg",0)
a=np.array(img)
m=len(a)
n=len(a[0])
for i in range(m):
    for j in range(n):
        if((j%2==0)and(i%2==0)):
            a[i][j]=255
        else:
            a[i][j]=0

#cv2.imshow("image",a)
cv2.imwrite("out.png",a)
