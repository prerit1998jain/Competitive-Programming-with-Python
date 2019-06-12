
'''
Minimum Swaps Problem

You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order

'''

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    length = len(arr)
    edge_cycles = []
    edge_cycle = []
    l = list(arr)
    val = list(range(length))
    output = 0
    # Creating the Graph 
    graph = {}
    for i in range(length):
        graph[i] = l[i]-1
    #print(graph)

    while(len(val) != 0):
        edge_cycle = []
        temp = val[0]
        while((temp not in edge_cycle)):
            edge_cycle.append(temp)
            #l.remove(arr[temp])
            val.remove(temp)
            temp = graph[temp]
        edge_cycles.append(edge_cycle)
        output += len(edge_cycle) - 1 
    return output


# Calling the function 
n = int(input("Enter the size of input array \n"))
arr = list(map(int, input("Enter the array elements separated by spaces").rstrip().split()))
res = minimumSwaps(arr)

print("Result: {}".format(res))

