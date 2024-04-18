
1. start Ubuntu 20.04
2. make sure ROS is installed, I'm using Noetic
3. open a few terminals and `cd` into `catkin_ws`
5. run `roscore` in a terminal
6. run `catkin_make` in a terminal to compile your "stuff" idk what it's called
7. run `roslaunch my_robot launch_robot_gazebo.launch` to start gazebo, a window should open (note: to close, you just to kill process "ctrl+c" on windows/linux, maybe "cmd+c" for mac? just be patient to wait for it to shut down completely rather than killing the PiD)
8. run `rosrun my_robot joint_control.py` in a terminal
9. click the start button to start sim
10. edit `src/my_robot/scripts/joint_control.py` file to change control input
11. edit `src/my_robot/urdf/urdf/mugatu_urdf.urdf.xacro` to change robot params
12. edit `src/my_robot/launch/launch_robot_gazebo.launch` to modify launch files
