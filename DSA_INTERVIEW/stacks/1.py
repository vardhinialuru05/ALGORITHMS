class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class Stack:
    def __init__(self,size = 100):
        self.head = None
        self.maxSize = size
        self.cSize = 0
    def empty(self):
        if self.head is None:
            return True 
        else:
            return False
    def full(self):
        if self.cSize  == self.maxSize:
            return True
        else:
            return False
    
    def push(self,data):
        if not self.full():
            newNode = Node(data)

            if self.head is None:
                self.head = newNode
            else:
                pointer = self.head
                while pointer.next is not None:
                    pointer = pointer.next
                pointer.next = newNode
            self.cSize += 1
        else:
            raise "stack is full"
    def pop(self):
        if not self.empty():
            if self.head.next is None:
                result = self.head.val
                self.head = None
            else:
                pointer = self.head
                while pointer.next.next is not None:
                    pointer = pointer.next
                result = pointer.next.val
                pointer.next = pointer.next.next

            self.cSize -=1
            return result
        else:
            raise "stack is empty"
    def peek(self):
        if self.empty():
            raise "stack is empty"
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            return pointer.val
    def __str__(self):
        stack = "["
        pointer = self.head
        while pointer.next is not None:
            stack += str(pointer.val) + "->"
            pointer = pointer.next
        stack += str(pointer.val) + "]"
        return stack

myStack = Stack(3)
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack)
myStack.pop()
print(myStack)

print(myStack.peek())