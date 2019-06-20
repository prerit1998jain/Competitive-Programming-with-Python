'''
PROBLEM SHERLOCK AND ANAGRAMS
Two strings are anagrams of each other if the letters of one string can be
rearranged to form the other string. Given a string, find the number of
pairs of substrings of the string that are anagrams of each other.

'''

'''
Approach is that,
First create a dictionary for each sequence consisting of number of letters of
a specific type it have.
Then check seq by seq whether they consist of same dictionary or not.
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
    # Looping over all sequences size
    for i in range(1,len(s)+1):
        sequences = []
        # storing the sequencees of size i in a list called SEQUENCES
        for k in range(len(s)-i+1):
            sequences.append(s[k:k+i])
        seq_dict = {}

        # Dictionary development
        for seq in sequences:
            seq_dict[seq] = {}
            if(seq[0] in list(seq_dict[seq].keys())):
                continue
            for letter in seq:
                if letter not in list((seq_dict[seq]).keys()):
                    seq_dict[seq][letter] = 1
                else:
                    seq_dict[seq][letter] += 1

        # Checking over sequences of similar length for ANAGRAMS
        for i in range(len(sequences)):
            for j in range(i+1,len(sequences)):
                k = 0
                temp1 = set(list(sequences[i]))
                for letter in temp1:
                    if(letter not in list((seq_dict[sequences[j]]).keys())):
                        break
                    else:
                        if(seq_dict[sequences[i]][letter] == seq_dict[sequences[j]][letter]):
                            k = k+1
                        else:
                            break

                if(k == len(temp1)):
                    count += 1
    return(int(count))

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
