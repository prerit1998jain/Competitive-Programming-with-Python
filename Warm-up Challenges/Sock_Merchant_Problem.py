#!/bin/python3

'''

Problem:-

John works at a clothing store. He has a large pile of socks that he must pair
by color for sale. Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

For example, there are n = 5 socks with colors [1,2,1,2,1] . There is one pair of
color 1 and one of color 2. There is 1 odd sock left, of color 1. The number of
spairs is 2.


'''

import math
import time
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant_1(n, ar):
    count = 0
    count_dict = Counter(ar)
    val = list(set(ar))
    for i in val:
        count += int(count_dict[i]/2)
    return count

def sockMerchant_2(n,ar):
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
    return(count)

arr = []
i = 0
n = int(input("Please input the number of socks \n"))
print(" Input the colors of the n socks \n")
for i in range(int(n)):
    value = input()
    arr.append(value)
print(arr)

start1 = time.time()
count1 = sockMerchant_1(n,arr)
end1 = time.time()
start2 = time.time()
count2 = sockMerchant_2(n,arr)
end2 = time.time()
print("1: Output: {}, Execution Time: {}".format(count1,(end1-start1)))
print("2: Output: {}, Execution Time: {}".format(count1,(end2-start2)))
