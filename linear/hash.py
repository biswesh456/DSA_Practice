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

linear_probing = True
quadratic_probing = False

class OpenDictionary:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.TOMBSTONE = '<DELETED>'

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def put(self, key, value):
        start_value = self.hash_function(key)
        hash_value = self.hash_function(key)
        
        if self.keys[hash_value] is None:
            self.keys[hash_value] = key
            self.values[hash_value] = value
        
        else:
            if self.keys[hash_value] == key:
                self.values[hash_value] = value
            else:
                if linear_probing:
                    new_hash_value = self.linear_rehash(hash_value)

                    while self.keys[new_hash_value] is not None and self.keys[new_hash_value] != self.TOMBSTONE and self.keys[new_hash_value] != key and new_hash_value != start_value:
                        new_hash_value = self.linear_rehash(new_hash_value)

                    if self.keys[new_hash_value] is None or self.keys[new_hash_value] == self.TOMBSTONE:
                        self.keys[new_hash_value] = key
                        self.values[new_hash_value] = value
                    
                    elif self.keys[new_hash_value] == key:
                        self.values[new_hash_value] = value

                    else:
                        print('Increase hash size!!')
                    
    def get(self, key):
        start_value = self.hash_function(key)
        hash_value = self.hash_function(key)

        if self.keys[hash_value] == key:
            return self.values[hash_value]

        else:
            if linear_probing:
                new_hash_value = self.linear_rehash(hash_value)

                while self.keys[new_hash_value] is not None and start_value != new_hash_value:
                    if self.keys[new_hash_value] == key:
                        return self.values[new_hash_value]
        
                    new_hash_value = self.linear_rehash(new_hash_value)
                
                return None

    def delete(self, key):
        start_value = self.hash_function(key)
        hash_value = self.hash_function(key)

        if self.keys[hash_value] == key:
            self.keys[hash_value] = self.TOMBSTONE
            self.values[hash_value] = None            

        else:
            if linear_probing:
                new_hash_value = self.linear_rehash(hash_value)

                while self.keys[new_hash_value] is not None and start_value != new_hash_value:
                    if self.keys[new_hash_value] == key:
                        self.keys[new_hash_value] = self.TOMBSTONE
                        self.values[new_hash_value] = None
                        break
                    else:
                        new_hash_value = self.linear_rehash(new_hash_value)        
        

    def linear_rehash(self, key):
        return (key + 1) % self.size


    def hash_function(self, key):
        return abs(hash(key)) % self.size  # hash is an in-build python function to get hash values for every immutable object.


D1 = OpenDictionary(3)
D1['A'] = 1
D1['B'] = 4
D1['C'] = 2

print(D1.keys, D1.values)

D1['C'] = 10
D1['B'] = 7
D1['D'] = 18
print(D1.keys, D1.values)
print(D1['D'], D1['C'])

D1.delete('C')
print(D1.keys, D1.values)
D1['D'] = 18
print(D1.keys, D1.values)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class ClosedDictionary:

    def __init__(self, size):
        self.size = size
        self.keys = [None] * size

    def __str__(self):
        output = ''
        for i in range(self.size):
            if self.keys[i] is None:
                output += 'None | '
            else:
                current_node = self.keys[i]
                while current_node is not None:
                    output += f'{current_node.key} : {current_node.value} -> '
                    current_node = current_node.next
                
                output = output[:-3] + '| '
        
        return output[:-3]

    
    def put(self, key, value):
        hash_value = self._hash_function(key)

        if self.keys[hash_value] is None:
            # Create the first head
            head_node = Node(key, value)
            self.keys[hash_value] = head_node
        else:
            current_node = self.keys[hash_value]
            while current_node.next is not None and current_node.key != key:
                current_node = current_node.next
            
            if current_node.key == key:
                current_node.value = value
            else: 
                current_node.next = Node(key, value)

    def get(self, key):
        hash_value = self._hash_function(key)

        if self.keys[hash_value] is None:
            return None
        else:
            current_node = self.keys[hash_value]
            while current_node.next is not None and current_node.key != key:
                current_node = current_node.next
            
            if current_node.key == key:
                return current_node.value
            else: 
               return None

    def delete(self, key):
        hash_value = self._hash_function(key)

        if self.keys[hash_value] is None:
            return None
        
        else:
            current_node = self.keys[hash_value]
            if current_node.key == key:
                self.keys[hash_value] = current_node.next
                return None

            while current_node.next is not None and current_node.next.key != key:
                current_node = current_node.next
            
            if current_node.next is None:
                return None
            elif current_node.next.key == key:
                current_node.next = current_node.next.next

    # We generally do it when a linkedlist hits a threshold length             
    def rehash(self):
        self.size = self.size * 2
        old_keys = self.keys
        self.keys = [None] * self.size

        for node in old_keys:
            current_node = node
            while current_node is not None:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next

    def _hash_function(self, key):
        return abs(hash(key)) % self.size 


D2 = ClosedDictionary(3)
D2.put('d', 22)
D2.put('e', 22)
D2.put('q', 3)
D2.put('d', 20)
D2.put('s', 10)
D2.put(123, 1)
print(D2)
print(D2.get('q'), D2.get(123))
D2.delete('q')
print(D2)
D2.put('x', 'qw')
D2.put('y', 'll')
D2.put('z', 'nb')
print(D2)
D2.rehash()
print(D2)
