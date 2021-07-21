#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from week2.srv import compute_ang_vel,compute_ang_velRequest,compute_ang_velResponse
from geometry_msgs.msg import Twist

radius = 0
angular_velocity = 0

def node3():
    
    global angular_velocity

    def callback(msg):

        global radius
        global angular_velocity 
        radius = msg.data
        ang_velocity_getter = rospy.ServiceProxy('ang_velocity_giver', compute_ang_vel)
        req = compute_ang_velRequest()
        req.radius = radius
        res = ang_velocity_getter(req)
        angular_velocity = res.ang_velocity 
        # print(angular_velocity)
        # print("This is in callback")
        	
    
    rospy.init_node('turtlenode')

    sub = rospy.Subscriber('radius', Float32, callback)
    pub = rospy.Publisher('cmd_vel',Twist, queue_size = 10)
    rospy.loginfo('Waiting for the service server')
    rospy.wait_for_service('ang_velocity_giver')
    rospy.loginfo('Access granted to the service server')
    rate = rospy.Rate(2)
    print(angular_velocity)
    print("This is in main")
    
    
    #for iter in range(5):#
    while not rospy.is_shutdown():
        
        move = Twist()
        move.linear.x = 0.1
        move.angular.z = angular_velocity
        
        #print(angular_velocity)
        pub.publish(move)
        rate.sleep()
        #rospy.sleep(60)




if __name__ == '__main__':
    try:
        node3()
    except rospy.ROSInterruptException:
        pass