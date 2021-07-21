#!/usr/bin/env python

import rospy
from std_msgs.msg import String
a = 'a'
b = 'b'
def node3():

	def callback(msg):
		global a 
		a = msg.data	
	def callback2(msg):
		global b 
		b = msg.data



	rospy.init_node('node_3')
	sub = rospy.Subscriber('hello', String, callback)
	sub = rospy.Subscriber('world', String, callback2)
	pub = rospy.Publisher('helloworld',String, queue_size = 10)

	rate = rospy.Rate(2)

	while not rospy.is_shutdown():
		pub.publish(a + b)
		rate.sleep()
if __name__ == '__main__':
    try:
        node3()
    except rospy.ROSInterruptException:
        pass
