# Find the largest between two indices and keep swapping it left till we reach the left most. 
# Run it again but only for n-1 tims this time.

# Adaptive algorithm is something where best case is different than worst case. If we give it a sorted algorithm then it should understand it and not do it's worst complextiy.

arr = [3, 6, 66, 32, 88, 9, 23, 100, 302, 301, 978, 33, 1, 99999, 1212]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(arr))

# How can I make it adaptive? 
# Have a flag = 0 and if in the round, there is any swap then make flag = 1. If flag remains 0 in the pass then the array is now already sorted.
# If flag = 1 at the end then in the next round again make flag = 0 and check for next pass again

def adaptive_bubble_sort(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break
    return arr

arr = [3, 6, 66, 32, 88, 9, 23, 100, 302, 301, 978, 33, 1, 99999, 1212]
print(adaptive_bubble_sort(arr))

# What is a stable algorithm?
# If two values are same then the ones which were before in the original array should also come before in the sorted array.
# If we sort wrt first digit of number and 43 comes before 41 then 43 should come before 41 even in sorted algo.
# Bubble sort is stable.