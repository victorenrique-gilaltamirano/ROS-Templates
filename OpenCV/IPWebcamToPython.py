import cv2
import numpy as np

#############################
# REQUIREMENT
# Install "IP Webcam" app https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US
# From Pavel Khlebovich
# Start Server
# Pay close attention to the IP address
#############################

cap = cv2.VideoCapture('https://192.168.2.104:8080/video') # insert IP address/video

while(True):

    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

cap.release()

cv2.destroyAllWindows()
