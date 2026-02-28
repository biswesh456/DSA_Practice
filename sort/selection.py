# Here we select the index and find the best for that index
# It does less swaps. So its faster than bubble sort(but we cant say for adaptive bubble sort).
# Selective sort is not adaptive.

# Lets do it for descending

def selection_sort(arr):
    for i in range(len(arr)-1):
        max = i
        for j in range(i+1, len(arr)):
            if arr[max] < arr[j]:
                max = j
        
        arr[i], arr[max] = arr[max], arr[i]

    return arr
            
arr = [3, 6, 66, 32, 88, 9, 23, 100, 302, 301, 978, 33, 1, 99999, 1212]
print(selection_sort(arr))