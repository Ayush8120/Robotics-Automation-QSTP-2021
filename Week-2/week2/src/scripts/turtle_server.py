#!/usr/bin/env python3

import rospy

from week2.srv import compute_ang_vel

def give_me_ang_velocity(request): #x: float,y: float,theta: float,v: float,w:float):
    v = 0.1
    radius = request.radius
    ang_velocity = v/radius 
    return ang_velocity


rospy.init_node('turtle_service_server') # init node
service = rospy.Service('ang_velocity_giver', compute_ang_vel, give_me_ang_velocity) #service teller 
rospy.spin()
