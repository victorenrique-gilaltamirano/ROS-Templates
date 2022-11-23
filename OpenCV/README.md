# Install OpenCV in ROS

1. Open a terminal and update with `$ sudo apt-get update`.
2. Upgrade with `$ sudo apt-get upgrade`.
3. (For ROS Kinetic, for example) Install OpenCV with `$ sudo apt-get install libopencv-dev ` OR `$ sudo apt-get install ros-kinetic-opencv3`. For Noetic: `$ sudo apt-get install ros-noetic-vision-opencv`.
4. Verify installation: in a new terminal type `$ python`, and then `import cv2`, no errors should be generated.

In case of having troubles with `imshow`:
Run in terminal:
```
sudo apt-get install libopencv-*
pip install opencv-contrib-python
```
Use `pip3` if using Python3

## Additional packages
1. Install ROS USB cam package, in a new terminal type `$ sudo apt-get ros-kinetic-usb-cam`.
2. And ROS Image View, with `$ sudo apt-get install ros-kinetic-image-view`.

# Bridging Images between OpenCV and ROS
Treat Image as a message travelling through a topic. However the image format supported by ROS is different and NOT coompatible with the image format used by OpenCV. CvBridge enables the conversion between formats.

# Read webcam as image message for ROS
In a new terminal type `$ rosrun usb_cam usb_cam_node _pixel_format:=yuyv`.

Verify in a new terminal `rostopic list`, and the `usb_cam/image_raw` topic should appear listed, which is the topic containing the webcam image as ROS message format.

Additionally, in a new terminal view the image by `$ rosrun image_view image_view image:=/usb_cam/image_raw`.
