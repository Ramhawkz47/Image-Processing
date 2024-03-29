import numpy as np
import cv2
import time

cap = cv2.VideoCapture(2)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    try:
        cv2.imshow('cam',frame)
    except:
        print("No webcam!!!")
        time.sleep(1)
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
