#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import math
import time

def hip_joint_control():
    rospy.init_node('hip_joint')

    # Adjust this to the correct topic for your robot's joint controller
    pub = rospy.Publisher('/mugatu_urdf/hip_joint_position_controller/command', Float64, queue_size=10)


    rate = rospy.Rate(150)  # 10 Hz
    start_time = time.time()

    while not rospy.is_shutdown():
        current_time = time.time()
        # Sinusoidal input for the joint position
        # amplitude = 0.349066 / 2
        amplitude = 0.18
        frequency = 1.6
        ang_freq = 2 * math.pi * frequency
        position = amplitude * math.sin(ang_freq * (current_time - start_time))

        # Publish the joint position
        pub.publish(position)

        rate.sleep()

if __name__ == '__main__':
    try:
        hip_joint_control()
    except rospy.ROSInterruptException:
        pass
