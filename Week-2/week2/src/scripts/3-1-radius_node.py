#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def rad_node():
    rospy.init_node('radius_node')
    pub = rospy.Publisher('radius', Float32, queue_size = 10)

    rate = rospy.Rate(2)
    r = 1
    while not rospy.is_shutdown():
        pub.publish(r)
        rate.sleep()

if __name__ == '__main__':
    try:
        rad_node()
    except rospy.ROSInterruptException:
        pass