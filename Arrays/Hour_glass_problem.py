'''
## 2D ARRAY - DS

We define an hourglass in an array A to be a subset of values with indices falling in this pattern in array's graphical representation:
a b c
  d
e f g
Hour_glass_sum is the sum of hour glass elements of a particular pattern. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

'''


import time
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    template_arr = [[1,1,1],[0,1,0],[1,1,1]]
    size = len(arr)
    hour_glass_score = []
    for i in range(size-2):
        for l in range(size-2):
            sum = 0
            for j in range(i,i+3):
                for k in range(l,l+3):
                    sum = sum + template_arr[j-i][k-l]*arr[j][k]
            hour_glass_score.append(sum)
        #print(sum,"\n")
    return(max(hour_glass_score))

# Function Execution
arr = []

size = int(input("Enter the size of the squared array array \n"))

for _ in range(size):
    arr.append(list(map(int, input("Enter the 2-D array row-wise, each element separated by spaces  \n").rstrip().split(" "))))
start = time.time()
result = hourglassSum(arr)
print("The output is ", result, "\n")
end = time.time()
print("Execution time is ", (end - start))
