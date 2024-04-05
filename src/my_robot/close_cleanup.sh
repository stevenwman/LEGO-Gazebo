#!/bin/bash

rosnode kill -a

killall gzserver gzclient

echo "All Gazebo and ROS nodes have been terminated."
