
'''


'''
import time


def insertion_sort(arr):
    length = len(arr)
    if length == 1:
        return
    else:
        val = arr[length-1]
        j = length - 2
        insertion_sort(arr[0:j])
        while j >= 0 and val < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = val
    return arr


# Taking input
n = int(input("Enter the size of array \n"))
arr = list(map(int, input("Enter the {} values separated by spaces \n".format(n)).rstrip().split()))
start = time.time()
sorted = insertion_sort(arr.copy())
end = time.time()

print("Input array: {}\n Sorted Array: {} \n Execution Time: {}".format(arr,sorted,end-start))
    
