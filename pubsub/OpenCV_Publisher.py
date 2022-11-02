#!/usr/bin/env python3
"""
________________
|  Node:       |    Image.msg
| video_pub.py |----------------->
|              |  /video_frames
_______________|

"""
 
import rospy 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge 
import cv2
  
if __name__ == '__main__':
  rospy.init_node('video_pub_py', anonymous=True)
  
  pub = rospy.Publisher('video_frames', Image, queue_size=10)
  
  rate = rospy.Rate(10) # 10hz
  
  cap = cv2.VideoCapture(0)
  
  br = CvBridge()
  
  while not rospy.is_shutdown():
    ret, frame = cap.read()
         
      if ret == True:
       
        rospy.loginfo('publishing video frame')
             
        pub.publish(br.cv2_to_imgmsg(frame))
             
      rate.sleep()
