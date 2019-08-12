#!/usr/bin/python
import inputanalyzer
import grid
import rover

import numpy as np
import re

'''
Main class of the program
'''

# function to show instructions and get user input
def askInput():
    print("====================================================================")
    print("|Welcome to the NASA program to control the robotic rovers on Mars!|")
    print("====================================================================")
    print("Instructions:")
    print("\t- Enter the right corner coordinates of the plateau, to set the size of it.")
    print("\t- Then enter the robotic rovers initial position, direction and the set of commands they have to execute.")
    print("\t\t - All coordinates are 2D, and have to be entered separated by a space.")
    print("\t\t - Directions have to be introduced: N for north, S for south, E for east and W west.")
    print("\t\t - Commands that the rover can execute are: L for turn to left. R for turn to right and M to move.")
    print("\t- To end the input prompt write a . in a sigle line")
    print()
    print("Example:")
    print("INPUT\t\t\t\tOUTPUT")
    print("5 5\t\t\t\t1 3 N")
    print("1 2 N\t\t\t\t5 1 E")
    print("LMLMLMLMM\t\t\t\t")
    print("3 3 E\t\t\t\t")
    print("MMRMMRMRRM\t\t\t\t")
    print(".\t\t\t\t")
    print()

    input_list = []
    while True:
        input_str = input("")
        if input_str == ".":
            break
        else:
            input_list.append(input_str)

    return input_list

# from the analyzer get user plateu coordinates as numpy float array
def getCoordinatesFromInput(analyzer):
    gridcoord = analyzer.getPlateuCoordinates()
    temp = gridcoord.split()
    temp2 = np.array(temp)
    topright = temp2.astype(np.float)

    return topright

# given user direction by letter, return corresponding numpy array of the direction
def getDir(letter):
    if letter == 'N':
        return np.array([0.0,1.0])
    
    if letter == 'S':
        return np.array([0.0,-1.0])

    if letter == 'E':
        return np.array([1.0,0.0])

    if letter == 'W':
        return np.array([-1.0,0.0])

# from the user input in the analyzer, create robotic robers object list
def getRoboticRoversList(analyzer):
    commands = analyzer.getRoverLines()
    rovers = []
    pos = []
    direction = []
    cmdlist = [] 

    for c in commands:
        posdirmatch = re.search("\d+( )+\d+( )+[NSEW]$", c)
        commandsmatch = re.search("[LRM]+$", c)
        
        if posdirmatch:
            tmp = c.split()
            tmp = tmp[:2]
            tmp2 = np.array(tmp)
            pos = tmp2.astype(np.float)
            tmp = c.split()
            direction = getDir(tmp[2:][0])

        if commandsmatch:
            cmdlist = list(c)

        if (commands.index(c)+1) % 2 == 0:
            rob = rover.Rover(pos,direction,cmdlist)
            rovers.append(rob)

    return rovers

def main():
    
    # Display instructions and ask for user input
    userinput = askInput()

    # Analyze and extract user input
    analyzer = inputanalyzer.InputAnalyzer(userinput)

    # Get top right coordinates of the plateau from user input
    topright = getCoordinatesFromInput(analyzer)

    # Create robotic rovers list from user input
    rovers = getRoboticRoversList(analyzer)

    # Create grid
    plateau = grid.Grid(topright,rovers)

    # Compute robotic rovers final positions and directions and display it
    plateau.updateGrid()
    plateau.gridStatus()

# call to main
main()