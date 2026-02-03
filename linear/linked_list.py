# Linear data structure which is a collection of nodes conraining data and address.
# Advantage over array - Insertion and deletion (O(1)) can be done quickly and we do not have to shift all the other indices.
# Advantage over array - In dynamic array, we waste a bit of memory because of additional indices we have beforehand. In linkedlist the memory is non-contiguous.
# Advantage over array - More suitable for building stacks, queues, doubly linked list and circular linked list.

# Disadvantage over dynamic array - Read operation is O(n) unlike dynamic array which is O(1).

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def getVal(self):
        return self.val
    
    def getNext(self):
        return self.next

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

    def insert_head(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        self.len += 1

    def insert_index(self, index, val):
        if index > self.len:
            return f'{index} is getter than total number of nodes'

        if index == 0:
            self.insert_head(val)

        curr = self.head
        for i in range(index-1):
            curr = curr.next
        
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        self.len += 1

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
            print(curr.val)
            curr = curr.next

l = MyLinkedList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.append(4)
l.traverse()
l.insert_index(5, 6)
l.insert_index(2, 10)
l.insert_index(0, 100)
l.insert_index(7, 1000)
print(l)

    
                



    


        