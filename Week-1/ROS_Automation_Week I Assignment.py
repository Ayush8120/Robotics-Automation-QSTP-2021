"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w) 
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt
import math

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        """
        Write the Kinematics model here
        Expectation:
            1. Given v, w and the current state self.x, self.y, self.theta
                and control commands (v, w) for n timesteps, i.e. n * dt seconds,
                return the final pose (x, y, theta) after this time.
            2. Append all intermediate points into the self.x_points, self.y_points list
                for plotting the trajectory.
        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps
        Return:
            x, y, theta (float): final pose 
        """
        for iter in range(n):
            self.theta = w*self.dt + self.theta
            self.x = v*self.dt*math.cos(self.theta) + self.x
            self.y = v*self.dt*math.sin(self.theta) + self.y
            self.x_points.append(self.x)
            self.y_points.append(self.y)

        return self.x, self.y, self.theta

    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        # plt.savefig(f"Unicycle_{v}_{w}.png")

if __name__ == "__main__":
    print("Unicycle Model Assignment")

    robot = Unicycle(0, 0, 0,0.1)
    final_x , final_y , final_theta = robot.step(1,0.5,25)
    robot.plot(v = 1.0,w = 0.5)

    # robot = Unicycle(0, 0, 1.57,0.2)
    # final_x , final_y , final_theta = robot.step(0.5,1,10)
    # robot.plot(v = 0.5,w = 1)

    # robot = Unicycle(0, 0, 0.77,0.05)
    # final_x , final_y , final_theta = robot.step(0.5,1,50)
    # robot.plot(v = 5,w = 4)


    # print(final_x)
    # print(final_y) 
    # print(final_theta)
    # make an object of the robot and plot various trajectories