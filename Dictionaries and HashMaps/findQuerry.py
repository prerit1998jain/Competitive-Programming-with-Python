'''
Problem: findQueries
You are given  queries. Each query is of the form two integers described below:
1-x  : Insert x in your data structure.
2-y  : Delete one occurence of y from your data structure, if present.
3-z  : Check if any integer is present whose frequency is exactly .
If yes, print 1 else 0.

'''


'''
Approach
Rather than keeping only one dictionary of frequencies, keep two dictionaries
one mapping integer to frequency and other mapping frequency to counts.

Using a single dictionary will lead to worse time complexiety.

Use of Counter() Library is useful.
'''

#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    freq = Counter()
    cnts = Counter()
    #print(freq,cnts)
    arr = []

    for querry in queries:
        if querry[0]==1:
            cnts[freq[querry[1]]] -= 1
            freq[querry[1]] += 1
            cnts[freq[querry[1]]] += 1
        elif querry[0]==2 and freq[querry[1]] > 0:
            cnts[freq[querry[1]]] -= 1
            freq[querry[1]] -= 1
            cnts[freq[querry[1]]] += 1
        elif querry[0] == 3:
            if(cnts[querry[1]] > 0):
                arr.append(1)
            else:
                arr.append(0)
    return arr


    # for querry in queries:
    #     print(querry)
    #     if(querry[0] == 1):
    #         freq[querry[1]] += 1
    #         cnts[freq[querry[1]]

    #     elif(querry[0] == 2):
    #         if(querry[1] in dic.keys()):
    #             dic[querry[1]] -= 1

    #     elif(querry[0] == 3):
    #         if querry[1] in dic.values():
    #             arr.append(1)
    #         else:
    #             arr.append(0)

    # return(arr)

#  Calling the function

q = int(input().strip())
queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
ans = freqQuery(queries)

print(ans)
