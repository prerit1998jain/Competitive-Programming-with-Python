'''
PROBLEM: MINIMUM BOUQUET'S PRICE

A group of friends want to buy a bouquet of flowers. The florist wants to maximize
his number of new customers and the money he makes. To do this, he decides he'll
multiply the price of each flower by the number of that customer's previously
purchased flowers plus 1. The first flower will be original price,(0+1)*original price
, the next will be (1+1)x original price and so on.

Given the size of the group of friends, the number of flowers they want to purchase
and the original prices of the flowers, determine the minimum cost to purchase all
of the flowers.
'''

'''
APPROACH:
1) Sort the array in reverse order.
2) Calculate the num of pass, each has to go. (len(cost)//k) and remainder.
3) Add the costs accordingly.

'''

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse = True)
    minCost = 0
    num = len(c)//k
    rem = len(c)%k
    p = 0
    while(p<num):
        for i in range(p*k,(p+1)*k):
            minCost += (p+1)*c[i]
        p+=1
    for j in range(rem):
        minCost += (p+1)*c[num*k + j]

    return(minCost)

# Function CALLING
nk = input("Enter the number of flowers, and number of friends separated by spaces \n").split(" ")
n = int(nk[0])
k = int(nk[1])

c = list(map(int,input("Enter the costs \n").rstrip().split()))
minCost = getMinimumCost(k,c)

print("MINIMUM COST: ", minCost)
