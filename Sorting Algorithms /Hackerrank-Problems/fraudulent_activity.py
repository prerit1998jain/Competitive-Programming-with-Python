'''
PROBLEM FRAUDULENT ACTIVITY NOTIFICATIONS
HackerLand National Bank has a simple policy for warning clients about possible
fraudulent account activity. If the amount spent by a client on a particular day
is greater than or equal to 2x the client's median spending for a trailing number
of days, they send the client a notification about potential fraud. The bank
doesn't send the client any notifications until they have at least that trailing
number of prior days' transaction data.
Given the number of trailing days d and a client's total daily expenditures for a
period of n days, find and print the number of times the client will receive a
notification over all n days.
'''

import math
import os
import random
import re
import sys
import statistics
from collections import Counter

'''Intelligent Approach
   You keep count of d elements every time, and as sliding window moves, you
   just have to calculate the count of just one more number, and skipping
   extra counting for calculating the frequency each time you calculate the
   median.
'''

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

    ''' Naive Approach:

        Every D elements you calculate the median through statistics, which
        takes order of n time to do so. Hence causing timeout for most of the
        examples.

    '''
    # notification = 0
    # for i in range(d,len(expenditure)):
    #      median = statistics.median(expenditure[i-d:i])
    #      if expenditure[i] >= median*2:
    #          notification += 1
    # return(notification)

nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditur
