#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def node2():
	rospy.init_node('node_2')
	pub = rospy.Publisher('world', String, queue_size = 10)

	rate = rospy.Rate(2)

	while not rospy.is_shutdown():
		pub.publish("World!")
		rate.sleep()
if __name__ == '__main__':
    try:
        node2()
    except rospy.ROSInterruptException:
        pass
