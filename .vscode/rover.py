import numpy as np

'''
Class to represent a robotic rover and his possible actions.
'''

class Rover:
    def __init__(self, posini, ndir, cmds):
        self.pos0 = posini
        self.pos = self.pos0
        self.dir = ndir
        self.instructions = cmds

    # function to turn the robotic rover heading direction to the right
    def turnRight(self):
        alpha = -np.pi/2
        newx = float(round(np.cos(alpha)*self.dir[0] - np.sin(alpha)*self.dir[1]))
        newy = float(round(np.sin(alpha)*self.dir[0] + np.cos(alpha)*self.dir[1]))
        self.dir = np.array([newx,newy])

    # function to turn the robotic rover heading direction to the left
    def turnLeft(self):
        alpha = np.pi/2
        newx = float(round(np.cos(alpha)*self.dir[0] - np.sin(alpha)*self.dir[1]))
        newy = float(round(np.sin(alpha)*self.dir[0] + np.cos(alpha)*self.dir[1]))
        self.dir = np.array([newx,newy])

    # function to move the robotic rover from its position to the corresponding direction
    def move(self):  
        newx = self.pos[0] + self.dir[0]*1
        newy = self.pos[1] + self.dir[1]*1
        self.pos = np.array([newx,newy])

