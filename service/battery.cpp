/*
##############
# Node name: "battery"
# 
# Service Client in the "/set_led" topic with the service SetLed.srv definition
# ~~~~~~~~~~~~~
# my_robot_msgs/SetLed.srv is defined as:
# int64 led_number
# int64 state
# ---
# bool success
################
*/

#include <ros/ros.h>

#include <my_robot_msgs/SetLed.h>

#define STATE_FULL 1
#define STATE_EMPTY 2

void set_led(ros::NodeHandle *nh, int battery_state) {
	ros::service::waitForService("/set_led");

	ros::ServiceClient client = 
		nh->serviceClient<my_robot_msgs::SetLed>("/set_led");

	my_robot_msgs::SetLed srv;
	srv.request.led_number = 1;
	srv.request.state = 0;
	if (battery_state == STATE_EMPTY) {
		srv.request.state = 1;
	}

	if (client.call(srv)) {
		ROS_INFO("Set led success flag: %d", srv.response.success);
	}
	else {
		ROS_WARN("Service call failed");
	}
}

int main (int argc, char **argv) {
	ros::init(argc, argv, "battery");
	ros::NodeHandle nh;

	int battery_state = STATE_FULL;

	while (ros::ok()) {
		ros::Duration(7.0).sleep();
		battery_state = STATE_EMPTY;
		ROS_INFO("Battery is empty!");
		set_led(&nh, battery_state);
		ros::Duration(3.0).sleep();
		battery_state = STATE_FULL;
		ROS_INFO("Battery is now full");
		set_led(&nh, battery_state);
	}
}
