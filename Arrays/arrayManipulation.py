'''
PROBLEM ARRAY arrayManipulation
Starting with a 1-indexed array of zeros and a list of operations,
for each operation add a value to each of the array element between two given indices, inclusive.
Once all operations have been performed, return the maximum value in your array.

'''

'''
SOLUTION:
The solution is very efficient.
For Each querry we just add the increment to the first element and
decrease the (q+1)th element by decrement value.
'''

import math
import os
import random
import re
import sys

# arrayManipulation Problem
def arrayManipulation(n, querries):
    queries = list(queries)
    arr = []
    x = 0
    maximum = 0
    for i in range(n+1):
        arr.append(0)
        for querry in queries:
        arr[querry[0]-1] += querry[2]
        if(querry[1]< n):
            arr[querry[1]] -= querry[2]

        for i in list(arr):
        x = x+i
        if(x>maximum):
            maximum = x
    return(maximum)

# Calling the function
nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])

querries = []

for _ in range(m):
    querries.append(list(map(int,input("Input Space separated querry \n").rstrip().split(" "))))

result = arrayManipulation(n,querries)
print("The result is {} \n".format(result))
