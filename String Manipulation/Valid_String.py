'''
Problem: SHERELOCK AND VALID STRINGS

Sherlock considers a string to be valid if all characters of the string appear
the same number of times. It is also valid if he can remove just  character at
index in the string, and the remaining characters will occur the same number of
times. Given a string , determine if it is valid. If so, return YES, otherwise
Return NO.

'''

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    count = Counter(s)
    flag = 0
    count_values = Counter(list(count.values()))
    arr = list(count_values.keys())
    #print(arr)
    if(len(arr)>2):
        return("NO")
    if(len(arr)==2):
        if (count_values[arr[0]]) > 1 and count_values[arr[1]] > 1:
            return("NO")
        if(abs(arr[0]-arr[1]))>1:
            if(count_values[arr[0]] == 1 and arr[0] != 1):
                return("NO")
            if(count_values[arr[1]] == 1 and arr[1] != 1):
                return("NO")
            else:
                return("YES")
        else:
            return("YES")
    else:
        return("YES")

## fUNCTION CALLING
s = input("INPUT STRING\n")
result = isValid(s)
print(result,"\n")
