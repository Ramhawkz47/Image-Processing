import cv2
import numpy as np

def words(x):
    z=[]
    for l in x:
        s=""
        for c in l:
            for b in c:
                if(((b>=97)and(b<=122))or((b>=65)and(b<=90))):
                    s+=chr(b)
        z.append(s.lower())
    return z

img = cv2.imread('img.jpg')
a=np.array(img)
l=words(a)
for i in range(len(l)):
    x={}
    for c in l[i]:
        x[c]=0
    s=""
    for c in x:
        s+=c
    l[i]=s
    print(l[i])
