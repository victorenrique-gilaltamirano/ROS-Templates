# Install OpenCV in ROS

1. Open a terminal and update with `$ sudo apt-get update`.
2. Upgrade with `$ sudo apt-get upgrade`.
3. (For ROS Kinetic, for example) Install OpenCV with `$ sudo apt-get install libopencv-dev ` OR `$ sudo apt-get install ros-kinetic-opencv3`.
4. Verify installation: in a new terminal type `$ python`, and then `import cv2`, no errors should be generated.

## Additional package
1. Install ROS USB cam package, in a new terminal type `$ sudo apt-get ros-kinetic-usb-cam`.
2. And ROS Image View, with `$ sudo apt-get install ros-kinetic-image-view`.
