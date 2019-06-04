'''

# Left Rotations

Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

'''


import math
import os
import random
import re
import sys
import time

# Complete the rotLeft function below.
def rotLeft(a, d):
    length = len(a)
    rem = d%length
    result = []
    for i in range(rem,length):
        result.append(a[i])
    for i in range(rem):
        result.append(a[i])

    return(result)


# Calling the function

nd = input("Enter the size of the array and order of rotation separated by spaces: \n").split()

n = int(nd[0])
d = int(nd[1])

a = list(map(int, input("Enter the array elements\n").rstrip().split()))
start = time.time()
result = rotLeft(a,d)
end = time.time()
print("The input array is {} \n".format(a))
print("The resultant array after {} rotations is {} \n".format(d, result))
print("The execution time is {}\n".format(end - start))
