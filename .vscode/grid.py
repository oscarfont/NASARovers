import numpy as np
import sys

'''
Class to represent the Plateau, with its list of coordinates and list of Robotic Rovers.
'''

class Grid:
    def __init__(self, toprightcoord, roverslist):
        self.topright = toprightcoord
        self.points = self.initGrid()
        self.rovers = roverslist

    # function to generate an array of points from the top right coordinates of the Plateau
    def initGrid(self):
        temp = []
        for i in range(int(self.topright[0])+1):
            for j in range(int(self.topright[1])+1):
                temp.append(np.array([i,j]))
        
        return np.array(temp).astype(np.float)

    # function to move robotic rovers with the user instructions to see which is their end position and direction
    def updateGrid(self):
        for rover in self.rovers:
            for l in rover.instructions:
                if l == "L":
                    rover.turnLeft()
                if l == "R":
                    rover.turnRight()
                if l == "M":
                    rover.move()
                    if not self.checkPosition(rover.pos):
                        sys.exit('ERROR: One of the robotic rovers ends up outside of the plateau because of invalid instructions or initial position')

    # function to display the robotic rover final position and direction
    def gridStatus(self):
        print()
        for rover in self.rovers:
            self.displayResult(rover)

    # given a direction numpy array, return the corresponding letter
    def getDirLetter(self,direction):
        # North
        if np.array_equal(direction,np.array([0.0,1.0])):
            return 'N'
        
        # South
        if np.array_equal(direction,np.array([0.0,-1.0])):
            return 'S'

        # East
        if np.array_equal(direction,np.array([1.0,0.0])):
            return 'E'

        # West
        if np.array_equal(direction,np.array([-1.0,0.0])):
            return 'W'


    # function that given a robotic rover creates final postion and direction string to display
    def displayResult(self,rover):
        # position
        x = str(int(rover.pos[0]))
        y = str(int(rover.pos[1]))

        #direction
        d = self.getDirLetter(rover.dir)
        
        #output
        out = x + " " + y + " " + d

        print(out) 

    # function to check if a given position is inside the Plateau or not
    def checkPosition(self, pos):
        for point in self.points:
            if(np.array_equal(pos,point)):
                return True
                break
        return False