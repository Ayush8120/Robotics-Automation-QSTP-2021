#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def node1():
	rospy.init_node('node_1')
	pub = rospy.Publisher('hello', String, queue_size = 10)

	rate = rospy.Rate(2)

	while not rospy.is_shutdown():
		pub.publish("Hello, ")
		rate.sleep()
if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
