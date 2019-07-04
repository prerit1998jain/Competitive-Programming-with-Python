
'''
Minimum Swaps Problem

You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order

'''

'''
The solution is that if we replace each element to it's correct position and some cycles will be formed and the number of swaps required per cycle is len(cycle) - 1
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
    print("The graph formed : {} \n".format(graph))

    # Checking the length of the list val, as I am removing the node which is moved to it's correct postion
    while(len(val) != 0):
        edge_cycle = []
        temp = val[0]
	# Start of new edge_cycle
        while((temp not in edge_cycle)):
            edge_cycle.append(temp)
            val.remove(temp)
            temp = graph[temp]
        edge_cycles.append(edge_cycle)
        output += len(edge_cycle) - 1
    return output

# APPROACH 2
# def minimumSwaps(arr):
#     temp = [0] * (len(arr) + 1)
#     for pos, val in enumerate(arr):
#         temp[val] = pos
#         #pos += 1
#     swaps = 0
#     for i in range(len(arr)):
#         if arr[i] != i+1:
#             swaps += 1
#             t = arr[i]
#             arr[i] = i+1
#             arr[temp[i+1]] = t
#             temp[t] = temp[i+1]
#     return swaps




# Calling the function
n = int(input("Enter the size of input array \n"))
arr = list(map(int, input("Enter the array elements separated by spaces").rstrip().split()))
res = minimumSwaps(arr)

print("Result: {}".format(res))
