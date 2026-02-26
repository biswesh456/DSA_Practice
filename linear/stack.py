# Last In First Out
# We can actually easily convert a python list into stack because it already hss an append and a pop. Peek can be L[-1].

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class StackLL:
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.len += 1

    def pop(self):
        if self.head is None:
            return 'Empty Stack!!'
        val = self.head.val
        self.head = self.head.next
        self.len -= 1
        return val
    
    def peek(self):
        if self.head is None:
            return 'Empty Stack!!'

        return self.head.val

    def is_empty(self):
        return self.head == None

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.val};", end='')
            curr = curr.next

        print()
    
    def size(self):
        return self.len

s = StackLL()
s.push(1)
s.push(2)
s.push(3)
s.traverse()
print(s.pop())
s.traverse()
print(s.peek())

def text_editor(text, pattern):
    u = StackLL()
    r = StackLL()

    for i in text:
        u.push(i)

    for p in pattern:
        if p == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)

    res = ''
    while not u.is_empty():
        res = u.pop() + res

    print(res)

text_editor('Kolkata', 'uurrurur')





def find_celeb(L):
    s = StackLL()
    for i in range(len(L)):
        s.push(i)

    while s.size() >= 2:
        i = s.pop()
        j = s.pop()

        if L[i][j] == 0:
            s.push(i)
        else:
            s.push(j)
    
    celeb = s.pop()

    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                print('No one is a celebrity')
                return

    print(f'{celeb} is the celebrity')


L = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]
find_celeb(L)


# Create a queue using two stacks
class QueueUsingStack():
    def __init__(self):
        self.enq_stack = StackLL()
        self.deq_stack = StackLL()
    
    def enqueue(self, val):
        self.enq_stack.push(val)
    
    def dequeue(self):
        if self.deq_stack.head is None:
            if self.enq_stack.head is None:
                return 'Queue empty'
            while self.enq_stack.head is not None:
                self.deq_stack.push(self.enq_stack.pop())
            
        return self.deq_stack.pop()

    def traverse(self):
        result = ''
        deq_pointer = self.deq_stack.head
        enq_pointer = self.enq_stack.head

        while deq_pointer is not None:
            result += str(deq_pointer.val) + ' '
            deq_pointer = deq_pointer.next
        
        result = result[:-1]

        temp_res = '' 
        while enq_pointer is not None:
            temp_res = str(enq_pointer.val) + ' ' + temp_res
            enq_pointer = enq_pointer.next

        result += ' ' + temp_res

        return result.strip()       

print('===== Queue Using 2 Stacks =====')
q = QueueUsingStack()
q.enqueue(3)
q.enqueue(6)
q.enqueue(7)
print(q.traverse())
print(q.dequeue())
print(q.traverse())
q.dequeue()
print(q.traverse())
q.enqueue(2)
q.enqueue(1)
q.enqueue(0)
print(q.traverse())
q.dequeue()
print(q.traverse())

