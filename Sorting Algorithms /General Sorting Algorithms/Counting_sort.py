'''
COUNTING SORT

'''

'''
APPROACH:

It uses a sorting technique based on keys between a specific range. It works by
counting number of objects having distinct key values. Then doing some airthmetic
to calculate the position of each object in the output sequence.
'''

from collections import Counter
from collections import defaultdict

def counting_sort(arr):
    max_val = max(arr)
    count = [0]*max
    print(count)
    array = [0]*len(arr)

    for x in (arr):
        count[x] += 1

    for i in range(1,max):
        count[i] = count[i-1] + count[i]
    print(count)
    for i in range(len(arr)):
        ans[i] =


# Taking input
n = int(input("Enter the size of array \n"))
arr = list(map(int, input("Enter the {} values separated by spaces \n".format(n)).rstrip().split()))
start = time.time()
sorted = counting_sort(arr.copy())
end = time.time()
