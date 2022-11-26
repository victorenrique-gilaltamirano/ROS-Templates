#!/usr/bin/env python3

##############
# Node name: "number_counter"
# Subscribed to "/number" topic, carrying the message type Int64.msg
# Publishing to "/number_count" topic the message type Int64.msg
# 
# Service Server of "/reset_counter" topic carrying the service type SetBool.srv
#
# ~~~~~~~~~~~~~
# std_msgs/Int64.msg is defined as:
# int64 data
# ~~~~~~~~~~~~~
# sts_srvs/SetBool.srv is defined as:
# bool data
# ---
# bool success
# string message
################

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool


class NumberCounter:

	def __init__(self):
		self.counter = 0

		self.number_subscriber = rospy.Subscriber("/number", Int64, self.callback_number)

		self.pub = rospy.Publisher("/number_count", Int64, queue_size=10)

		self.reset_service = rospy.Service("/reset_counter", SetBool, self.callback_reset_counter)

	def callback_number(self, msg):
		self.counter += msg.data
		new_msg = Int64()
		new_msg.data = self.counter
		self.pub.publish(new_msg)

	def callback_reset_counter(self, req):
		if req.data:
			self.counter = 0
			return True, "Counter has been successfully reset"
		return False, "Counter has not been reset"


if __name__ == '__main__':
	rospy.init_node('number_counter')
	NumberCounter()
	rospy.spin()
