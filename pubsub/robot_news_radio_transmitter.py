#!/usr/bin/env python3

##############
# Node name: "robot_news_radio_transmitter"
# 
# Publishing to "/robot_news_radio" topic the message type String.msg
# 
# ~~~~~~~~~~~~~
# std_msgs/String.msg is defined as:
# string data
################

import rospy
from std_msgs.msg import String

if __name__ == '__main__':

	rospy.init_node('robot_news_radio_transmitter', anonymous=True)

	pub = rospy.Publisher("/robot_news_radio", String, queue_size=10)

	rate = rospy.Rate(2)

	while not rospy.is_shutdown():
		msg = String()
		msg.data = "Hi, this is Dan from the Robot News Radio !"
		pub.publish(msg)
		rate.sleep()

	rospy.loginfo("Node was stopped")
