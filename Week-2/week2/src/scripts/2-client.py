#!/usr/bin/env python3
import rospy
from week2.srv import *
import sys
import matplotlib.pyplot as plt
def plot(x_points,y_points,v,w):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(x_points, y_points, color="red", alpha=0.75)
        plt.grid()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        #plt.savefig(f"Unicycle_{v}_{w}.png")

rospy.init_node('service_client')
rospy.loginfo("Waiting for the service!")
rospy.wait_for_service('trajectory_giver')
rospy.loginfo("Received the service!")

trajectory_getter = rospy.ServiceProxy('trajectory_giver', trajectory)
req = trajectoryRequest()
req.x = float(sys.argv[1]) 
req.y = float(sys.argv[2])
req.theta = float(sys.argv[3])
req.v = float(sys.argv[4])
req.w = float(sys.argv[5])

# print(req.theta)
# print(req.v)
# print(req.w)
res = trajectory_getter(req)
#print('AYUSH')
#print(res.x_points)
#print(type(res.y_points))
x_points = list(res.x_points.data)
y_points = list(res.y_points.data)
plot(x_points, y_points, req.v, req.w)
