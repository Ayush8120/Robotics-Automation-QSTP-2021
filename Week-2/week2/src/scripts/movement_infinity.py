#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
import math
#from tf2_msgs.msg import TFMessage
from nav_msgs.msg import Odometry


x =0
y =0
z =0
angular_velocity = 0

# class trio:

#     def __init__(self,x: float, y: float , z: float):
#         self.x = x
#         self.y = y
#         self.z = z
def callback(msg):
    global x
    global y
    global z 
    # x = msg.twist.twist.linear.x
    # y = msg.twist.twist.linear.y
    # z = msg.twist.twist.linear.z
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z
    #print(x)
    # trio_object = trio(x,y,z)

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
    #print('x:' + str(x))
    #print('y:' + str(y))
    print('Out of both loops!')
    print('x' + str(abs(x)))
    print('y' + str(abs(y)))
    
    #if (rospy.get_time()//tme)%2 == 0:
    #if (v*rospy.get_time()//dst)%2 == 1:
    # while (v*rospy.get_time()//dst)%2 == 1:
    now = rospy.get_time()
    while (rospy.get_time() - now) <= tme:    
        move = Twist()
        move.linear.x = 0.1
        move.angular.z = 1*angular_velocity
        pub.publish(move)
        print('anticlock')
        rate.sleep()

    while abs(x) >= 0.0473683069933 or abs(y) >= 0.00997247856854:
        move = Twist()
        move.linear.x = 0.1
        move.angular.z = 1*angular_velocity
        pub.publish(move)
        print('anticlock-push')
        rate.sleep()
        change = 1

    now = rospy.get_time()
    
    while (rospy.get_time() - now) <= tme:

        move = Twist()
        move.linear.x = 0.1
        move.angular.z = -1*angular_velocity
        pub.publish(move)
        print('clock')
        rate.sleep()

    while abs(x) >= 0.0473683069933 or abs(y) >= 0.00997247856854:
        print(x)
        print(y)
        move = Twist()
        move.linear.x = 0.1
        move.angular.z = -1*angular_velocity
        pub.publish(move)
        print('clock-push')
        rate.sleep()


# if __name__ == '__main__':
#     try:
#         movement_infinity_node()
#     except rospy.ROSInterruptException:
#         pass
# movement_infinity_node()