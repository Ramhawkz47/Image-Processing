import cv2
import numpy as np
import pickle

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

d={}
with open("data.pickle",'rb') as f:
    d=pickle.load(f)

img = cv2.imread('img.jpg')
a=np.array(img)
l=words(a)
for i in l:
    for j in range(len(i)-1):
        if((i[j]=="h")and(i[j+1]=="e")):
            #print(i+"   "+str(j)
            print("he",end=" ")
            

