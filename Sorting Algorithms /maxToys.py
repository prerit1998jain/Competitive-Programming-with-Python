import math
import os
import random
import re
import sys
import time

def maximumToys(prices,k):
    prices.sorted()
    sum = 0
    for i in range(len(prices)):
        sum += prices[i]
        if sum > prices:
            return(i)
            break

# Taking inputs
nk = input("Enter the total number of toys and budget \n").split()
n = int(nk[0])
k = int(nk[1])

prices = list(map(int,input().rstrip().split()))

start = time.time()
result = maximumToys(prices,k)
end = time.time()

print("Maximum Toys: {}, Execution time: {}".format(result,end-start))
