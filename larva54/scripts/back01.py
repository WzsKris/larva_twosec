#!/usr/bin/python

import rospy
from std_msgs.msg import Float64

def main():
    rospy.init_node('limb_position_control')

    # Publishers for position controllers
    pubList = [
        rospy.Publisher('/joint02_position_controller/command', Float64, queue_size=8),
        rospy.Publisher('/joint04_position_controller/command', Float64, queue_size=8),
        rospy.Publisher('/joint06_position_controller/command', Float64, queue_size=8),
        rospy.Publisher('/joint08_position_controller/command', Float64, queue_size=8),
        rospy.Publisher('/joint09_position_controller/command', Float64, queue_size=8),
        rospy.Publisher('/joint11_position_controller/command', Float64, queue_size=8),
        rospy.Publisher('/joint13_position_controller/command', Float64, queue_size=8),
        rospy.Publisher('/joint15_position_controller/command', Float64, queue_size=8)
    ]

    rate = rospy.Rate(5)

    positions = [0.2, -0.2]

    index = 0
    while not rospy.is_shutdown():
        pos = positions[index % 2]

        for pub in pubList:
            pub.publish(Float64(pos))

        print(f"Set joints to position: {pos}")
        index += 1

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print("Program interrupted before completion")
