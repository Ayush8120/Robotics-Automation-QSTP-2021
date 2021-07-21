#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
import math
from nav_msgs.msg import Odometry


x =0
y =0
z =0
angular_velocity = 0

def callback(msg):
    global x
    global y
    global z 
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z
    
rospy.init_node('movement_infinity_node')
pub = rospy.Publisher('cmd_vel',Twist, queue_size = 10)
sub = rospy.Subscriber('odom',Odometry, callback)

rate = rospy.Rate(2)
v = 0.1
radius = 1

angular_velocity = v/radius
tme = (2*math.pi*radius/v) 
dst = 2*math.pi*radius
now = rospy.get_time()

while not rospy.is_shutdown():
    #print('Out of both loops!')
    #print('x' + str(abs(x)))
    #print('y' + str(abs(y)))
    
    now = rospy.get_time()
    while (rospy.get_time() - now) <= tme:    
        move = Twist()
        move.linear.x = 0.1
        move.angular.z = 1*angular_velocity
        pub.publish(move)
        #print('anticlock')
        rate.sleep()

    while abs(x) >= 0.0473683069933 or abs(y) >= 0.00997247856854:
        move = Twist()
        move.linear.x = 0.1
        move.angular.z = 1*angular_velocity
        pub.publish(move)
        #print('anticlock-push')
        rate.sleep()
        

    now = rospy.get_time()
    
    while (rospy.get_time() - now) <= tme:

        move = Twist()
        move.linear.x = 0.1
        move.angular.z = -1*angular_velocity
        pub.publish(move)
        #print('clock')
        rate.sleep()

    while abs(x) >= 0.0473683069933 or abs(y) >= 0.00997247856854:
        print(x)
        print(y)
        move = Twist()
        move.linear.x = 0.1
        move.angular.z = -1*angular_velocity
        pub.publish(move)
        #print('clock-push')
        rate.sleep()



