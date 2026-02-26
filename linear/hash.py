# Hashing gives us fast searching - O(1) for searching
# Have a long array and have a hashing function which will convert the value into an index number where you can store the value in the array. 
# Like that you know exactly where the value is stored in the array through the hashing function.

# Hashing Function - Can be anything like a value % size of array. But then there should not be any 'collision' in the arrays.
# Collision can be solved using two methods - 1) Closed addressing 2) Open Addressing

# Closed addresing - If there is a collision then our values' address should not change.

# Chaining is a closed addressing technique. here the arrays contain nodes which contain the data and the next. So if there is a collision then we just create a new node and add it to the next of the previous node in the same index.
# But to avoid the linked list becoming too long on one index, we do re-hashing. There is a threshold called load factor. If it crosses then we increase the size of the original array and re-do the whole hashing of all the numbers including the previous ones.
# We can also use a binary tree instead of linked list as the searching is log(n)

# Open addressing - We can change the address of the current values if there is a collision.

# Linear Probing is a type of open addressing. Here if there is a collision then just check the next object till you find an empty place. Make sure that the array has atleast one empty space.
# So hashing function becomes [h(i) + k(i')] % size of array where h(i) is the normal hashing function, k(i') starts with 0 but increases by one every time the indices are not empty. But if it increases beyond the size then back to 0th index and search again.
# Quadratic Probing is also a type of open addressing where k(i') is not increased linearly by one but it increases quadratically.

class Dictionary:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, value):
        
