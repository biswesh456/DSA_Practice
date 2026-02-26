# First in First Out

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __str__(self):
        pointer = self.head
        result = ''
        while pointer is not None:
            result += str(pointer.val) + '<'
            pointer = pointer.next
        
        return result[:-1]


    def enqueue(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
            self.len += 1
        else:
            node = Node(val)
            self.tail.next = node
            self.tail = node
            self.len += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.next
            self.len -= 1
            if self.len == 0:
                self.tail = self.head

    def peek_head(self):
        if self.head is None:
            return 'Empty Queue'
        else:
            return self.head.val
    
    def peek_tail(self):
        if self.tail is None:
            return 'Empty Queue'
        else:
            return self.tail.val

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
q.dequeue()
print(q)
q.enqueue(1)
print(q)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q)
q.enqueue(1)
print(q.peek_head())
     
