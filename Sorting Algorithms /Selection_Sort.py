
import time
'''
SELECTION SORT
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
