'''
PROBLEM min Bribes
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride!
There are a number of people queued up, and each person wears a sticker
indicating their initial position in the queue. Initial positions increment by 1
from 1 at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap
positions. If two people swap positions, they still wear the same sticker denoting
their original places in line. One person can bribe at most two others.

'''
'''
APPROACH:
Any number can't be more than 2 positions ahead it's value. Since only two swaps
are allowed. So if that is the case, than print "Too chaotic"

Otherwise, run bubble_sort, as it just swap the adjacent elements. So, the number
of swaps required will be equal to the min swaps to reach the given chaotic
queue.
'''




import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def Bubble_sort(q):
    swaps = 0
    swap = 1
    while(swap != 0):
        swaps = swaps + swap
        swap = 0
        for i in range(len(q)-1):
            if (q[i]>q[i+1]):
                q[i],q[i+1] = q[i+1],q[i]
                swap = swap + 1
    return(q,swaps-1)


def minimumBribes(q):
    k = 0
    for i in range(len(q)):
        if(q[i]-1 > i+2):
            k = k + 1
    if (k == 0):
        q,swaps = Bubble_sort(q)
        print(swaps)

    else:
        print("Too chaotic")

t = int(input())

for t_itr in range(t):
    n = int(input())
    q = list(map(int, input().rstrip().split()))
    minimumBribes(q)
