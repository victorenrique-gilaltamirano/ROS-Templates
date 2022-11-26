#!/usr/bin/env python3

##############
# Node name: "led_panel"
# 
# Service Server in the "/set_led" topic with the service SetLed.srv definition
# ~~~~~~~~~~~~~
# my_robot_msgs/SetLed.srv is defined as:
# int64 led_number
# int64 state
# ---
# bool success
################

import rospy
from my_robot_msgs.srv import SetLed

led_states = [0,0,0]

def callback_set_led(req):
	led_number = req.led_number
	state = req.state
	global led_states

	if (led_number > len(led_states)) or (led_number <= 0):
		return False

	if not (state == 0 or state == 1):
		return False

	led_states[led_number - 1] = state

	return True

if __name__ == '__main__':
	rospy.init_node('led_panel')


	server = rospy.Service("/set_led", SetLed, callback_set_led)

	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		rospy.loginfo(led_states)
		rate.sleep()

