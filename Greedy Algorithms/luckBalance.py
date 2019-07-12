'''
PROBLEM: LUCK BALANCE PROBLEM
Lena is preparing for an important coding competition that is preceded by a
number of sequential preliminary contests. She believes in "saving luck", and
wants to check her theory. Each contest is described by two integers, L[i]  and T[i] :

L[i]: The amount of luck associated with a contest.
      If Lena wins the contest, her luck balance will decrease by ; if she loses it,
      her luck balance will increase by L[i].
T[i]: denotes the contest's importance rating. It's equal to 1 if the contest is important,
      and it's equal to 0 if it's unimportant.

If Lena loses no more than k important contests, what is the maximum amount of
luck she can have after competing in all the preliminary contests? This value
may be negative.

'''

import math
import os
import random
import re
import sys
from functools import cmp_to_key

def luck(contest):
    return(contest[0])

# Complete the luckBalance function below.
def luckBalance(k, contests):
    data = sorted(contests, key = luck, reverse = True)
    print(data)
    luck_score = 0
    lost = 0
    for i in (data):
        if i[1] == 0:
            luck_score += i[0]
        elif i[1] == 1 and lost < k:
            luck_score += i[0]
            lost += 1
        else:
            luck_score -= i[0]
    return(luck_score)


# FUNCTION CALLING
nk = input("ENTER THE VALUES OF n AND k separated by spaces \n").split(" ")
n = nk[0]
k = nk[1]

for _ in range(n):
    contests.append(list(map(int,input("Enter the luck and importance").rstrip().split())))

result = luckBalance(k, contests)

print("RESULT:", result, "\n")
