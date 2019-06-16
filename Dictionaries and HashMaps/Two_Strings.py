'''
PROBLEM: TWO STRINGS

Given two strings, determine if they share a common substring.
A substring may be as small as one character. For example, the words
"a", "and", "art" share the common substring .
The words "be" and "cat" do not share a substring.

'''


import math
import os
import random
import re
import sys

# APPROACH 1
def twoStrings(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    out = []

    intersection = list(set(s1) & set(s2))

    if len(intersection) == 0:
        out.append("NO")

    else:
        out.append("YES")

    return(out[0])

# APPROACH 2
  #  for i in s1:
  #      j += 1
  #      if(i in s2):
  #          out.append("YES")
  #          break

  #  if(j == len(s1)-1):
  #    out.append("NO")

  #  return(out)

# CALLING THE FUNCTION
q = int(input("ENTER THE NUMBER OF PAIRS \n"))

for q_itr in range(q):
    s1 = input("string 1 \n")

    s2 = input("string 2 \n")

    result = twoStrings(s1, s2)
    print(result)
