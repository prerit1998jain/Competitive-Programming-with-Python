'''
PROBLEM: SPECIAL STRING COUNTS

A string is said to be a special string if either of two conditions is met:
a) All of the characters are the same, e.g. aaa.
b) All characters except the middle one are the same, e.g. aadaa.
A special substring is any substring of a string which meets one of those criteria.
Given a string, determine how many special substrings can be formed from it.

'''


'''
Intelligent Approach: A 3 PASS solution.
Pass 1: Build a list consisting of entries, (char, consecutive_freq_char).
Pass 2: For every element, add (i*(i+1))/2 into the answer. (Special substrings
        of type 1)
Pass 3: Count the number of substrings of type 2.

Brute Force Approach: Counting every option.
'''


import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the substrCount function below.
def substrCount(n, s):
    count = 1
    ans = 0
    seq = []
    prev_char = s[0]

    # Pass 1
    for i,char in enumerate(s):
        if i != n-1 and i != 0:
            if char == prev_char:
                count+=1
                prev_char = char
            else:
                seq.append([prev_char,count])
                count = 1
                prev_char = char
        elif i == n-1:
            if char == prev_char:
                count+=1
                seq.append([prev_char, count])
            else:
                seq.append([prev_char, count])
                count = 1
                seq.append([char, count])

    #print(seq)
    # Pass 2
    for i in seq:
        ans += (i[1])*(i[1]+1)/2

    # Pass 3
    for i in range(len(seq)-2):
        if(seq[i][0]==seq[i+2][0] and seq[i+1][1]==1):
            ans += min(seq[i][1],seq[i+2][1])
            #print(seq[i:i+3])

    return(int(ans))


'''
Approach: 2 (Not intelligent)
'''
    # for i in range(2,n+1):
    #     count = defaultdict(int)
    #     k = 0
    #     for j in range(k,k+i):
    #         count[s[j]] += 1
    #     while(k < n-i+1):
    #         #print("0:",s[k:k+i],count,counts)
    #         if(len(count.keys())>2):
    #             k+=1
    #         elif len(count.keys())==2:
    #             if(i%2==0):
    #                 k+=1
    #             else:
    #                 #print(k + i//2 + 1)
    #                 if(count[s[k + i//2]]==1):
    #                     counts += 1
    #                     #print(s[k:k+i])
    #                     k+=1
    #                 else:
    #                     k += 1
    #         else:
    #             counts +=1
    #             #print(s[k:k+i])
    #             k+=1

    #         #print("1:",s[k:k+i], count, counts)
    #         count[s[k-1]] -= 1

    #         if k+i <= n:
    #             count[s[k+i-1]] += 1

    #         if(count[s[k-1]]==0):
    #             count.pop(s[k-1])
    #         #print("2: ",s[k:k+i], count, counts)


    # return(counts)

## Function Calling
n = int(input("Input the string size\n"))
s = input("Input the string \n")
result = substrCount(n, s)
print("Result:", Result, "\n")
