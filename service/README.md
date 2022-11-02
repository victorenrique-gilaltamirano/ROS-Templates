# Create new srv definition

For creating a new srv definition, we use primitive data types. Consult http://wiki.ros.org/msg

1. (skip if already done for msg) Create a package only for messages and service definitions, with `$ catkin_create_pkg my_robot_msgs roscpp rospy std_msgs`
2. (skip if already done for msg) Remove "include" folder with `$ rm -rf include/`
3. (skip if already done for msg) Remove "src" folder with `$ rm -rf src/`
We only need `CMakeLists.txt` and `package.xml`

4. (skip if already done for msg) Add in `package.xml`:
`<build_depend>message_generation</build_depend>`

`<exec_depend>message_runtime</exec_depend>`

5. (skip if already done for msg) Add in `CMakeLists.txt`:

`find_package(`

`...`

`message_generation`

`)`


`generate_messages(`

`...`

`std_msgs`

`)`


`catkin_package(`

`...`

`CATKIN_DEPENDS roscpp rospy std_msgs message_runtime`

`)`

6. Make a folder for srv definitions `$ mkdir srv`, containing a file, for example `$ touch ComputeDiskArea.srv`:

`float64 radius`

`---`

`float64 area`


7. Add this new file into the `CMakeLists.txt`:

`add_service_files(`

`  FILES`

`  ComputeDiskArea.srv`

`)`

8. Compile everything with `$ catkin_make`
