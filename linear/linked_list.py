# Linear data structure which is a collection of nodes conraining data and address.
# Advantage over array - Insertion and deletion (O(1)) can be done quickly and we do not have to shift all the other indices.
# Advantage over array - In dynamic array, we waste a bit of memory because of additional indices we have beforehand. In linkedlist the memory is non-contiguous.
# Advantage over array - More suitable for building stacks, queues, doubly linked list and circular linked list.

# Disadvantage over dynamic array - Read operation is O(n) unlike dynamic array which is O(1).

# The del function will actually delete others because of python's grabage collection. python maintains reference counting which is the list of things pointing to it. Once the head is deleted, there nothing pointing to the next node and hence that is deleted and so on.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def __len__(self):
        return self.len

    def __str__(self):
        curr = self.head
        string = ''
        while curr is not None:
            string += str(curr.val) + '->'
            curr = curr.next
        return string[:-2]

    def __getitem__(self, idx):
        curr = self.head
        pos = 0
        if idx < 0 or idx >= self.len:
            return 'index out of range'
        while curr is not None:
            if pos == idx:
                break
            curr = curr.next
            pos += 1
        
        return curr.val

    def insert_head(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        self.len += 1

    def insert_index(self, index, val):
        if index > self.len:
            return f'{index} is getter than total number of nodes i.e. {self.len}'

        if index == 0:
            return self.insert_head(val)

        curr = self.head
        for i in range(index-1):
            curr = curr.next
        
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        self.len += 1

    def insert_after(self, after, val):
        curr = self.head
        while curr is not None:
            if curr.val == after:
                new_node = Node(val)
                new_node.next = curr.next
                curr.next = new_node
                self.len += 1
                break
            else:
                 curr = curr.next
        
        if curr is None:
            return f'{after} not in the linked list'

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = Node(val)  
        
        self.len += 1
    
    def traverse(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.val};", end='')
            curr = curr.next

        print()

    def clear(self):
        self.head = None
        self.len = 0

    def delete_head(self):
        if self.head is None:
            return 'empty linked list'
        self.head = self.head.next
        self.len -= 1

    def pop(self):
        if self.head is None:
            return 'empty linked list'

        if self.head.next is None:
            val = self.head.val
            self.head = None
            self.len -= 1
            return val
        curr = self.head
        while curr.next.next is not  None:
            curr = curr.next
        
        val = curr.next.val
        curr.next = None
        return val

    def remove(self, val):
        if self.head is None:
            return 'empty linked list'

        curr = self.head
        while curr is not None and curr.next.val != val:
            curr = curr.next
        
        if curr is None:
            return 'value not found'
        else:
            curr.next = curr.next.next

    def search(self, val):
        curr = self.head
        pos = 0

        while curr is not None and curr.val != val:
            curr = curr.next
            pos += 1

        if curr is None:
            return 'value not found'
        
        else:
            return pos

    def reverse(self):
        prev = None
        curr = self.head
        
        while curr.next is not None:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward

        curr.next = prev
        self.head = curr

l = MyLinkedList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.append(4)
l.traverse()
l.insert_index(5, 6)
l.insert_index(2, 10)
l.insert_index(0, 100)
l.insert_index(6, 1000)
l.insert_after(2, 55)
print(l)
l.delete_head()
print(l)
print('popped', l.pop())
print('popped', l.pop())
print(l)
l.remove(55)
print(l)
l.reverse()
print(l)
l.reverse()
print(l)

    
                



    


        