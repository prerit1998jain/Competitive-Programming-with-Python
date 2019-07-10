'''
PROBLEM MAKING_ANAGRAMS

Alice is taking a cryptography class and finding anagrams to be very useful. We
consider two strings to be anagrams of each other if the first string's letters
can be rearranged to form the second string. In other words, both strings must
contain the same exact letters in the same exact frequency For example, bacdc and
dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption
is dependent on the minimum number of character deletions required to make the
two strings anagrams. Can you help her find this number?

'''
import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count = 0
    count_a = Counter((a))
    count_b = Counter((b))
    l = []
    for i in count_a.keys():
        count += abs(count_a[i]-count_b[i])
        l.append(i)
    for j in count_b.keys():
        if j not in l:
            count += abs(count_b[j]-count_a[j])

    return count


a = input("Enter String 1 \n")
b = input("Enter String 2 \n")
res = makeAnagram(a, b)
print("The number of deletions required is", res, '\n')
