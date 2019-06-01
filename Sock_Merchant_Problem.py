#!/bin/python3

'''
Problem:-

John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n = 5 socks with colors [1,2,1,2,1] . There is one pair of color 1 and one of color 2. There is 1 odd sock left, of color 1. The number of pairs is 2.
'''

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    used = []
    for i in range(n):
        if(i not in used):
            for j in range(i+1,n):
                if(j not in used):
                    if(ar[i] == ar[j]):
                        count = count + 1
                        used.append(j)
                        break
    return count

arr = []
i = 0
n = int(input("Please input the number of socks \n"))
print(" Input the colors of the n socks \n")
for i in range(int(n)):
    value = input()
    arr.append(value)

count = sockMerchant(n,arr)
print("The output is ", count)
