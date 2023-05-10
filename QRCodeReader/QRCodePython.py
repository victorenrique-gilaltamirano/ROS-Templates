## find a QR code in a webcam stream, surround the QR code in a box, and display the string content of QR code

import cv2
import numpy as np
from pyzbar.pyzbar import decode             ### pip install pyzbar

cap = cv2.VideoCapture(0) # acquiring image from webcam

#defining width of image, parameter 3
cap.set(3,640)
#defining hieght of image, parameter 4
cap.set(4,480)

while True:
    success, img = cap.read()
    
    for barcode in decode(img):
        
        myData = barcode.data.decode('utf-8')
        #print(myData)
        
        #for bounding box, we will use a polygon, then convert into array, 
        # and then send to draw
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        
        # put the data on top of the QR code
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
        
        
    cv2.imshow('Result',img)
    
    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
