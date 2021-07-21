#!/usr/bin/env python3

import rospy
import math

from week2.srv import trajectory,trajectoryResponse
from week2.msg import FloatList

def generate_trajectory(request): #x: float,y: float,theta: float,v: float,w:float):
    x = request.x
    y = request.y
    theta = request.theta
    v = request.v
    w = request.w
    n = 50
    dt = 0.05
    x_points = FloatList()
    y_points = FloatList()
    x_points_list = []
    y_points_list = []
    for iter in range(n):
        theta = w*dt + theta
        x = v*dt*math.cos(theta) + x
        y = v*dt*math.sin(theta) + y
        x_points_list.append(x)
        y_points_list.append(y)
    x_points.data = x_points_list
    y_points.data = y_points_list    
    return x_points, y_points


rospy.init_node('service_server') # init node
service = rospy.Service('trajectory_giver', trajectory, generate_trajectory) #service teller 
rospy.spin()
