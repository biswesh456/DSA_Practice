# Fixed size of a particular type
# Helps in going to various indices easily
# This is 'call by value'

# Referential array - Store the values in different places and then create an array and store only the Address of those values in that array. 
# Here, no need to use the same type because the address type is still the same for the array.
# This is 'call by reference'
# Eg. Python list
# Needs extra memory and is a bit slow. 

# Dynamic Array - Size adjusts based on the requirement and does not require to be provided with size from the begining.
# Basically, it is a static array where we always create a new array which is double the size of the current array, every time the array gets full.
# It is more of a concept and not anything physical. It is still static array.
# Python list is a dynamic array

# Check that list is indeed a dynamic referential array
import sys

l = []
for i in range(100):
    l.append(i)
    print(i, sys.getsizeof(l))

# create my own list
import ctypes
class mylist:
    def __init__(self):
        self.size = 1
        self.len = 0
        self.array = self._make_array(self.size)

    def __len__(self):
        return self.len
    
    # Create a c type array(static referential array) of a particular size
    def _make_array(self, size):
        return (size*ctypes.py_object)()

    def append(self, val):
        if self.len >= self.size:
            self.size = self.size*2
            temp_array = self._make_array(self.size)
            for i in range(self.len):
                temp_array[i] = self.array[i]
            self.array = temp_array
        
        self.array[self.len] = val
        self.len += 1

    def __str__(self):
        result = '['
        for i in range(self.len-1):
            result += str(self.array[i]) + ', '
        result += str(self.array[self.len-1]) + ']'
        return result

    def __getitem__(self, idx):
        if idx < self.len:
            return self.array[idx]
        else:
            return 'index out of range'

    def pop(self):
        if self.len == 0:
            return []
        val = self.array[self.len-1]
        self.len -= 1
        return val

    def clear(self):
        self.size = 1
        self.len = 0
        self.array = self._make_array(self.size)

    def index(self, val):
        for i in range(self.len):
            if self.array[i] == val:
                return i 
        
        return None

    def insert(self, val, idx):
        if self.len >= self.size:
            self.size = self.size*2

        temp_array = self._make_array(self.size)
        for i in range(idx):
            temp_array[i] = self.array[i]
        temp_array[idx] = val
        for i in range(idx, self.len):
            temp_array[i+1] = self.array[i]
        
        self.len += 1
        self.array = temp_array


l = mylist()
for i in range(10):
    l.append(i ** 2)

print(l)
print(l[2])
print(l.pop(), l)
print(l.index(16), l.index(33))
print(l)
l.insert(10, 4)
print(l)


    


