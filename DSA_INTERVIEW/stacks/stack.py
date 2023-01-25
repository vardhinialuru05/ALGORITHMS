class Stack:
    def __init__(self,size):
        self.list = []
        self.size = size

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.size:
            return True
        else:
            return False

    def push(self,data):
        if not Stack.isFull(self):
            self.list.append(data)
        else:
            raise "stack is full"

    def pop(self):
        if not Stack.isEmpty(self):
            self.list.pop()
        else:
            raise "stack empty"

    def __str__(self):
        result = "stack: ["
        for ele in self.list:
            result += str(ele) + ","
        result += "None]"
        
        return result

    def __len__(self):
        return len(list)
   
myStack = Stack(3)
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack)