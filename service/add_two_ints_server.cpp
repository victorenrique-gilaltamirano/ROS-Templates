/*
##############
# Node name: "add_two_ints_server"
# 
# Service Server in the "/add_two_ints" topic with the service AddTwoInts.srv definition
# ~~~~~~~~~~~~~
# rospy_tutorials/AddTwoInts.srv is defined as:
# int64 a
# int64 b
# ---
# int64 c
################
*/

#include <ros/ros.h>
#include <rospy_tutorials/AddTwoInts.h>

bool handle_add_two_ints(rospy_tutorials::AddTwoInts::Request &req,
						rospy_tutorials::AddTwoInts::Response &res)
{
	int result = req.a + req.b;
	ROS_INFO("%d + %d = %d", (int)req.a, (int)req.b, (int)result);
	res.sum = result;
	return true;
}

int main (int argc, char **argv) 
{
	ros::init(argc, argv, "add_two_ints_server");
	ros::NodeHandle nh;

	ros::ServiceServer server = nh.advertiseService("/add_two_ints",
		handle_add_two_ints);

	ros::spin();
}
