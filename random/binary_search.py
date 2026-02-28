# Only works on sorted array

def binary_search(arr, item, start):
    size = len(arr)
    if size == 0:
        return -1

    mid = size // 2

    if item == arr[mid]:
        return start + mid
    
    elif item < arr[mid]:
        return binary_search(arr[:mid], item, start)
    else:
        return binary_search(arr[mid+1:], item, mid+1)
        

arr = [3, 6, 66, 32, 88, 9, 23, 100, 302, 301, 978, 33, 1]
arr = sorted(arr)
print(arr)

print(binary_search(arr, 23, 0))


# Other way

def binary_search(arr, low, high, item):
    if low <= high:
        mid = (low + high) // 2
        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            return binary_search(arr, low, mid-1, item)
        else:
            return binary_search(arr, mid+1, high, item)
    else:
        return -1


arr = [3, 6, 66, 32, 88, 9, 23, 100, 302, 301, 978, 33, 1]
arr = sorted(arr)
print(arr)

print(binary_search(arr, 0, len(arr)-1, 23))
print(binary_search(arr, 0, len(arr)-1, 23222))