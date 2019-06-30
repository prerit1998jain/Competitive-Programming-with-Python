
import time
'''
SELECTION SORT
'''

'''
Approach
Traverse an array. And for each index, select the min element in the remaining
array and swap it with the current index.
'''

def Selection_Sort(arr):
    for i in range(n):
        min = i
        for j in range(i,(n)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return(arr)

# Taking input
n = int(input("Enter the size of array \n"))
arr = list(map(int, input("Enter the {} values separated by spaces \n".format(n)).rstrip().split()))
start = time.time()
sorted = Selection_Sort(arr)
end = time.time()

print("The Sorted Array is {}".format(sorted))
print("Execution time is {}".format(end-start))
