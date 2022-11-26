#!/usr/bin/env python3

# Node name: my_first_python_node
# Description: Displays in terminal the message "Hello" 10 times per second


import rospy

if __name__ == '__main__':
	rospy.init_node('my_first_python_node')
	rospy.loginfo("This node has been started")

	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		rospy.loginfo("Hello")
		rate.sleep()
