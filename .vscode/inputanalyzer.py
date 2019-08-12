import re
import sys

'''
Class to analyze and extract from the User input the Top Right Coordinates of the Plateau,
the initial position and direction and commands the Robotic Rovers will execute.
'''

class InputAnalyzer:
    def __init__(self, inputtxt):
        self.textinput = inputtxt

    def getPlateuCoordinates(self):
        # first input line
        coord = self.textinput[0]
        # RegEx the first line has to match
        match = re.search("\d+( )\d$", coord)
        
        # If the first command matches the RegEx, return, if not Invalid Syntax.
        if (match):
            return self.textinput[0]
        else:
            sys.exit('ERROR: Ivalid plateau coordinates')

    def getRoverLines(self):
        output = []

        for line in self.textinput:
            # RegExs of the commands accepted by the program
            plateau = re.search("\d+( )\d$", line)
            posdirmatch = re.search("\d+( )+\d+( )+[NSEW]$", line)
            commandsmatch = re.search("[LRM]+$", line)

            # if there are coordinates like the plateu, don't get them, we already have them
            if(plateau):
                continue
            
            # if it is the inital position and direction get them
            if(posdirmatch):
                output.append(line)
                continue

            # if it is a set of instructions get them
            if(commandsmatch):
                output.append(line)
                continue

            # if is nothing of the above mentioned, error
            sys.exit('ERROR: Ivalid rover coordiantes or instruction')

        return output
 