#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'doesCircleExist' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY commands as parameter.
#

def doesCircleExist(commands):
    # Write your code here
    # Init the axis for movement
    
    x = y = 0
    
             # codify the directions
    N = 0
    E = 1
    S = 2
    W = 3
    
    # set default to N
    direction = N
    
    tests = []
    
    # Traverse 
    for i in range(len(commands)):
    
        #get current move
        move = commands[i]
        
        # if current move is right or left, turn robot
        # divide by 4 to be always wihin 0, 1, 2, 3 range
        
        if move == 'R':
            direction = (direction + 1) % 4
        elif move == 'L':
            direction = (direction + 3) % 4
        else:
            # north, increment y axis
            if direction == N:
                y += 1
                print(y)
            # south, decrement y axis
            elif direction == S:
                y -= 1
                print(y)
            # east, increment x axis
            elif direction == E:
                x += 1
                print(x)
            # west, decrement x axis
            elif direction == W:
                x -= 1
                print(x)
        
            # if the sum of x and y moves is 0, we're in a circle
        if (x == 0 and y == 0):
            tests.append('YES')
        else:
            tests.append('NO')
    
    # print(tests)
    return tests
        
if __name__ == '__main__':

    commands = ['G']

    result = doesCircleExist(commands)
    print(result)

   
