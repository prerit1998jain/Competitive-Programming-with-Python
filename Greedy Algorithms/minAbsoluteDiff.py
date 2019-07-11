'''
PROBLEM: Minimum Absolute difference between any two array elements.
'''

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_val = math.inf
    for i in range(len(arr)-1):
        v = (arr[i+1] - arr[i])
        if v < min_val:
            min_val = v

    return(min_val)

# Calling the function

n = int(input("Enter the array size\n"))
arr = list(map(int, input("Enter the array elements separated by space").rstrip().split(" ")))
result = minimumAbsoluteDifference(arr)

print("MINIMUM ABSOLUTE DIFFERENCE:", result, "\n")
