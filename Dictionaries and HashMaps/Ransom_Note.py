
import math
import os
import random
import re
import sys
from collections import Counter

def checkMagazine(magazine, rasom):
    x = ((Counter(rasom) - Counter(magazine)) == {})
    if x == True:
        print("Yes")
    else:
        print("No")

    # magazine_dict = {}
    # note_dict = {}
    # #output = []
    # #print(magazine)
    # #print(note)
    # for word in magazine:
    #     if(word not in list(magazine_dict.keys())):
    #         magazine_dict[word] = 1
    #     else:
    #         magazine_dict[word] += 1

    # for word in note:
    #     if(word not in list(note_dict.keys())):
    #         note_dict[word] = 1
    #     else:
    #         note_dict[word] += 1

    # temp = set(note)
    # k = 0
    # for word in temp:
    #     if(word in note_dict and word in magazine_dict):
    #         if(note_dict[word] <= magazine_dict[word]):
    #             k = k+1
    #         else:
    #             break

    # if(k == len(temp)):
    #     print('Yes')
    # else:
    #     print('No')

    # for i in range(len(note)):
    #     #print(i)
    #     #print(note[i])
    #     if note[i] in list(magazine_dict.keys()):
    #         #print(note[i])
    #         if magazine_dict[note[i]] != 0:
    #             #print(note[i])
    #             magazine_dict[note[i]] -= 1
    #             temp = temp - 1
    #             #print(magazine_dict)
    #             #print(temp)

    #         else:
    #             output.append('No')
    #             #print("I am in \n")
    #             #return('No')
    #             break

    #     else:
    #         output.append('No')
    #         #print('I am in 2 \n')
    #         break

    # if (temp) == 0:
    #     output.append('Yes')
    # else:
    #     output.append('No')
    #     #print(note)
    #     #print('i am in 3\n')

    # print(output[0])
    # return 0
    # i = 0
    # for word in note:
    #     if(word in magazine):
    #         magazine.remove(word)
    #         i = i+1
    #     else:
    #         break

    # if(i == len(note)):
    #     print('Yes')
    # else:
    #     print('No')
