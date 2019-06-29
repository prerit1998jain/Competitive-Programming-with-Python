import math
import time

# Input the array size
n = int(input("Enter the size of array \n"))
q = list(map(int, input("Enter the {} values separated by spaces \n".format(n)).rstrip().split()))

def Bubble_sort_recursive(arr):
    flag = 0
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            flag = 1
            arr[i],arr[i+1]= arr[i+1],arr[i]
    if flag == 1:
        Bubble_sort_recursive(arr)

    return(arr)


arr = Bubble_sort_recursive(q)
print(arr)
