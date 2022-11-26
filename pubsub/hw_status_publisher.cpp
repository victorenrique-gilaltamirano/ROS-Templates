/*
##############
# Node name: "hardware_status_publisher"
#
# Publishing to "/my_robot/hardware_status" topic the message type HardwareStatus.msg
# 
# ~~~~~~~~~~~~~
# my_robot_msgs/HardwareStatus.msg is defined as:
# int64 temerature
# bool are_motors_up
# string debug_message
################
*/

#include <ros/ros.h>

#include <my_robot_msgs/HardwareStatus.h>

int main (int argc, char **argv) {
	ros::init(argc, argv, "hardware_status_publisher");
	ros::NodeHandle nh;

	ros::Publisher pub = nh.advertise<my_robot_msgs::HardwareStatus>(
		"/my_robot/hardware_status", 10);

	ros::Rate rate(5);

	while (ros::ok()) {
		my_robot_msgs::HardwareStatus msg;
		msg.temperature = 45;
		msg.are_motors_up = true;
		msg.debug_message = "Everything is running well";
		pub.publish(msg);
		rate.sleep();
	}
}
