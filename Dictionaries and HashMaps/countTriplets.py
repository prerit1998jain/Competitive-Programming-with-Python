'''
PROBLEM COUNTING triplets

You are given an array and you need to find number of tripets of indices (i,j,k)  such
that the elements at those indices are in geometric progression for a given
common ratio r and i<j<k .
'''


'''
Approach 2 doesn't take into account i<j<k constraint.
Approach 1 uses two dictionaries storing the following:
a) the number whose arrival will complete a doublet. (named pot_doublet that means potential doublets)
b) the number whose arrival will complete a triplet. (named pot_triplet)
'''

import math
import os
import random
import re
import sys
from collections import Counter
from collections import defaultdict
import time

# Approach 1
def countTriplets(arr, r):
    pot_doublet = defaultdict(int)
    pot_triplets = defaultdict(int)
    triplet = 0
    for i in arr:
        triplet += pot_triplets[i]
        doublet[i*r] += pot_doublets[i]
        pot_doublets[i*r] += 1
    return(triplet)

    # Approach 2
    # val = list(set(arr))
    # if r != 1:
    #     for i in range(len(val)):
    #         p = val[i]
    #         if((counts[p*r]>0)):
    #             if(counts[p*r*r]>0):
    #             #print(counts[p]*counts[p*r]*counts[p*r*r])
    #                 count += (counts[p]*counts[p*r]*counts[p*r*r])
    #         #counts[p] -= 1
    # else:
    #     for i in (val):
    #         if(counts[i]>=3):
    #             count += math.factorial(counts[i])/(math.factorial(counts[i] - 3)*6)
    # #print(triplets)
    #return(int(count))

# Calling the function


nr = input().rstrip().split()
n = int(nr[0])
r = int(nr[1])
arr = list(map(int, input().rstrip().split()))
start = time.time()
ans = countTriplets(arr, r)
end = time.time()

print("Answer is {}. Execution Time: {}".format(ans,(end-start)))
