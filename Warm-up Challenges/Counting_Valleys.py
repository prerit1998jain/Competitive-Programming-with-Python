'''
#### COUNTING VALLEYS PROBLEM ######

Gary is an avid hiker. He tracks his hikes meticulously, paying close attention
to small details like topography. During his last hike he took exactly n steps.
For every step he took, he noted if it was an uphill, U , or a downhill, D step.
Gary's hikes start and end at sea level and each step up or down represents a unit
change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step
up from sea level and ending with a step down to sea level. A valley is a sequence
of consecutive steps below sea level, starting with a step down from sea level
and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print
the number of valleys he walked through.

'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    value = 0
    steps = []
    #cons_U = 0
    #cons_D = 0
    count = 0
    for i in range(n):
        # Cheking sequentially the string Character and
        # determining the sea level after each step
        if(s[i] == 'U'):
            value += 1
            steps.append(value)

        else:
            value -= 1
            steps.append(value)
    
    # Checking for valleys
    for i in range(n):
        if i != 0 and steps[i] == 0 and steps[i-1] < 0:
            count += 1
    return count


## FUNCTION CALLING
n = int(input("Enter the number of steps \n"))
s = input("Enter the steps in the format of a string, 'U' for uphill step and 'D' for downhill step \n")
result = countingValleys(n, s)
print(result)
