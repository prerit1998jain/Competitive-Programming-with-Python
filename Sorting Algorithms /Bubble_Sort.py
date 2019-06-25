import math

# Input the array size
n = int(input("Enter the size of array \n"))
q = list(map(int, input("Enter the {} values separated by spaces \n".format(n)).rstrip().split()))

def Bubble_sort(q):
    swaps = 0
    swap = 1
    while(swap != 0):
        swaps = swaps + swap
        swap = 0
        for i in range(len(q)-1):
            if (q[i]>q[i+1]):
                q[i],q[i+1] = q[i+1],q[i]
                swap = swap + 1
    return(q,swaps)

p = []
p,n = Bubble_sort(q)
print(p,n)
