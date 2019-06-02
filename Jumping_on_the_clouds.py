'''
#### JUMPING ON THE CLOUDS PROBLEM

Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1  or 2. She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided. The number on each cloud is its index in the list. Give the least number of steps to be taken for winning.


'''

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    step_count = 0
    step = [0]
    i = 0
    # Checking the current cloud is not the last one.
    while(i < len(c) - 1):
	# checking if step size 2 is possible or not.
        if i+2 <= len(c)-1:
	    # Checking if step size 2 is feasibile or not.
            if c[i+2] == 0:
		# appending the step to the steps list
                step.append(i+2)
                step_count += 1
                i = i+2
            # if step size 2 isn't feasible, then go with step size 1
            else:
                if (i+1) <= len(c)-1:
                    step.append(i+1)
                    step_count += 1
                    i = i+1
        else:
            if i+1 <= len(c)-1:
                step.append(i+1)
                step_count += 1
                i = i+1 

    return step_count, step

# Calling the Function.

n = int(input("Enter the number of clouds \n"))
c = list(map(int, input("Enter the cloud type, i.e 0 for safe and 1 for thuderbolt  separated by spaces \n").rstrip().split()))
result = jumpingOnClouds(c)
print("The minimum no. of required steps are", result[0], " \nThe clouds on which he steped are ",result[1])
