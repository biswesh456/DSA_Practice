# Divide and Conquer
# Split the arrays till we get arrays of 1 element. Then start merging them.
# Its easier to merge 2 sorted arrays.
# Time complexity - nlogn, space complexity - 2n.
# Optimized code will have space complexity of only n which is only from the stack operations.
# it is not an adaptive algorithm.

def merge(arr1, arr2):
    i = 0
    j = 0

    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    merged.extend(arr2[j:])
    merged.extend(arr1[i:])

    return merged

a = [1, 10, 22]
b = [3, 5, 6]

print(merge(a, b))

def merge_sort(arr):
    l = len(arr)
    if l == 1:
        return arr
    
    mid = l // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

a = [2,10,5,222,13,1,88,9,31, 0]
print(merge_sort(a))

# If we dont want to store a separate array
def merge_optimized_for_space(arr1, arr2, arr):
    i = 0
    j = 0
    k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1

        k += 1
    
    while i < len(arr1):
        arr[k] = arr1[i]
        k += 1
        i += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        k += 1
        j += 1

def merge_sort_optimized(arr):
    l = len(arr)
    if l == 1:
        return arr
    
    mid = l // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort_optimized(left)
    merge_sort_optimized(right)

    merge_optimized_for_space(left, right, arr)

merge_sort_optimized(a)
print(a)