#!/usr/bin/env python3
"""
________________
|  Node:        |
| video_sub_py  |     Image.msg
|               |<-------------------
|               |     /video_frames
________________

"""

import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
 
def image_callback(data):
 
  # Used to convert between ROS and OpenCV images
  br = CvBridge()
 
  # Output debugging information to the terminal
  rospy.loginfo("receiving video frame")
   
  # Convert ROS Image message to OpenCV image
  current_frame = br.imgmsg_to_cv2(data)
   
  # Display image
  cv2.imshow("camera", current_frame)
   
  cv2.waitKey(1)
  
if __name__ == '__main__':
  
  rospy.init_node('video_sub_py', anonymous=True)
   
  sub = rospy.Subscriber('video_frames', Image, image_callback)
 
  rospy.spin()
 
  cv2.destroyAllWindows()
