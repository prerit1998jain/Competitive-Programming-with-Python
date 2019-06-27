import math
import time

# Input the array size
n = int(input("Enter the size of array \n"))
q = list(map(int, input("Enter the {} values separated by spaces \n".format(n)).rstrip().split()))

def Bubble_sort_recursive(arr):
    for i in range(len(arr)):
        one_pass(arr[0:(len(arr)-i)])
        print(arr)
    return(arr)

arr = Bubble_sort_recursive(q)
print(arr)
