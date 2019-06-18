'''
PROBLEM SHERLOCK AND ANAGRAMS
Two strings are anagrams of each other if the letters of one string can be
rearranged to form the other string. Given a string, find the number of
pairs of substrings of the string that are anagrams of each other.

'''

import math
import os
import random
import re
import sys
import time

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        sequences = []
        for k in range(len(s)-i+1):
            sequences.append(s[k:k+i])
        seq_dict = {}
        for seq in sequences:
            seq_dict[seq] = {}
            for letter in seq:
                if letter not in list((seq_dict[seq]).keys()):
                    seq_dict[seq][letter] = 1
                else:
                    seq_dict[seq][letter] += 1
        print(seq_dict)

        for seq1 in sequences:
            for seq2 in sequences:
                temp1 = set(list(seq1))
                temp2 = list(set(list(seq2)))
                for letter in temp1:
                    if(letter not in list((seq_dict[seq2]).keys())):
                        break
                    else:
                        if(seq_dict[seq1][letter] == seq_dict[seq2][letter]):
                            temp2.remove(letter)
                        else:
                            break

                if(len(temp2) == 0):
                    count += 1
        count -= len(sequences)
    return(int(count/2))

# APPROACH 2 (SIMPLE ARRAY TRAVERSAL)
        #print(sequences)
        # for seq1 in sequences:
            # for seq2 in sequences:
                # temp1 = list(seq1)
                # temp2 = list(seq2)
                # for letter in temp1:
                    # if(letter in temp2):
                        # temp2.remove(letter)
                    # else:
                        # break
                # if(len(temp2)==0):
                    # count += 1
        # count -= len(sequences)
    # return(int(count/2))

# CALLING function

q = int(input("ENTER THE NUMBER OF SEQUENCES \n"))

for q_itr in range(q):
    s = input("ENTER THE SEQUENCE \n")

    result = sherlockAndAnagrams(s)
    print(result, '\n')
    
