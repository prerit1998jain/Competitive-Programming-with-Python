'''
ACTIVITYNOTIFICATIONS PROBLEM
HackerLand National Bank has a simple policy for warning clients about possible
fraudulent account activity. If the amount spent by a client on a particular day
is greater than or equal to  the client's median spending for a trailing number
of days, they send the client a notification about potential fraud.
The bank doesn't send the client any notifications until they have at least that
trailing number of prior days' transaction data.
'''

'''
Approach 1:
a) We use frequency counter for finding out median. This ensures that we don't
count any thing twice.
b) We maintain a window of length d and store frequency values in it. We use
those to find out median.
c) We update the value of count array after every iteration.

Approach 2 uses median function from the statistics package, but it every time
computes the frequency counts for the d objects making it computationally expensive.
And it shows time out for most of the values

'''



import math
import os
import random
import re
import sys
import statistics
from collections import Counter
import time

# Median Function
def median(counts,mids):
    l = []
    for mid in mids:
        val = 0
        for i, key in enumerate(counts):
            val += key
            if val >= mid:
                l.append(i)
                break
    return(sum(l)/len(l))

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    # Counter
    notification = 0
    count = [0]*201

    # Index of medians
    mids = []
    if d%2 == 0:
        mids.append(d//2)
        mids.append(d//2 + 1)
    else:
        mids.append(d//2 + 1)

    for i in expenditure[:d]:
        count[i] += 1

    for i, exp in enumerate(expenditure[d:]):
        med = median(count, mids)

        if exp >= med*2:
            notification += 1

        old_val = expenditure[i]
        count[old_val] -= 1
        count[exp] += 1


    return(notification)


    # Approach 2
    # notification = 0
    # for i in range(d,len(expenditure)):
    #      median = statistics.median(expenditure[i-d:i])
    #      if expenditure[i] >= median*2:
    #          notification += 1
    # return(notification)

## Taking Inputs

nd = input("Enter the number of total days and number of trailing days \n").split(" ")

n = int(nd[0])
d = int(nd[1])

expenditure = list(map(int, input().rstrip().split()))

start = time.time()
result = activityNotifications(expenditure, d)
end = time.time()

print("The number of alerts sent: {} Execution Time: {}".format(result, end-start))
