import cv2
import numpy as np
from PIL import Image

def mati(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if(l[i][j]==1):
                l[i][j]=255

    return l


l=[[]]
i=0
f=open("data.txt","r")
for s in f:
    print(s)
    for c in s:
        if(len(l[i])==480):
           i+=1
           l.append([])
        else:
           y= bin(ord(c))[2:]
           for z in y:
               l[i].append(int(z))
    if(len(l)>640):
           break
f.close()
if(len(l[i])<480):
   x=480-len(l[i])
   for j in range(x):
       l[i].append(l[i][j])

if(len(l)<640):
    i=640-len(l)
    for j in range(i):
        l.append(l[j])

print(len(l))
print(len(l[0]))
img=np.array(mati(l),dtype=np.uint8)
print(img[0])
img = Image.fromarray(img, 'RGB')
cv2.imshow("image",img)
cv2.imwrite("/media/ramhawkz47/DATA/py",img)
