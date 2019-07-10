'''
PROBLEM ALTERNATING_CHARACTER

You are given a string containing characters  and  only. Your task is to change
it into a string such that there are no matching adjacent characters. To do this,
you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.
'''

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    t = 0
    delete = 0
    prev_char = None
    for i,char in enumerate(s):
        if i < len(s):
            #print(char)
            if char == prev_char:
                t += 1
                #print(t)

            else:
                if t>0:
                    delete += t
                t = 0
            prev_char = char

    delete += t

    return(delete)

## FUNCTION CALLING
s = input("Enter the string\n")
result = alternatingCharacters(s)
print(s)
