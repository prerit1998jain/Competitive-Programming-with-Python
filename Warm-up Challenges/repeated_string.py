'''
### REPEATED STRING PROBLEM

Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first n letters
of Lilah's infinite string.

'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    total_a = 0
    remainder_a = 0
    repeat = n // l
    remainder = n%l

    for i in range(l):
        if(s[i] == 'a'):
            total_a += 1

    for j in range(remainder):
        if(s[j]=='a'):
            remainder_a += 1

    return(total_a*repeat + remainder_a)

# Calling the function
s = input("Enter the string to be repeated \n")
n = int(input("Enter 'n' \n"))
result = repeatedString(s, n)

print(result)
