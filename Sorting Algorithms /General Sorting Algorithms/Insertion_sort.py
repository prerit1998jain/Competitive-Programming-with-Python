'''
Approach: Traverse the array. place the current element arr[i] into sorted Array
arr[0:i-1].
'''
import time

def Insertion_Sort(temp):
    arr = temp.copy()
    for i in range(len(arr)):
        val = arr[i]
        for j in range(1,i):
            if(val < arr [0]):
                arr.pop(i)
                arr.insert(0,val)
            elif(val > arr[j-1] and val < arr[j]):
                arr.pop(i)
                arr.insert(j,val)
            elif(val > arr[i-1]):
                break
    return(arr)

# Taking input
n = int(input("Enter the size of array \n"))
arr = list(map(int, input("Enter the {} values separated by spaces \n".format(n)).rstrip().split()))
start = time.time()
sorted = Insertion_Sort(arr)
end = time.time()

print("Input array: {}\n Sorted Array: {} \n Execution Time: {}".format(arr,sorted,end-start))
