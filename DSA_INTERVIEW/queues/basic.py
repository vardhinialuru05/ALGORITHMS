from queue import Queue, LifoQueue
#implementation of both queues nd stack
myQueue = Queue()
#this is stack
myStack = LifoQueue()

myQueue.put(10)
myQueue.put(20)
myQueue.put(30)

myStack.put(10)
myStack.put(20)
myStack.put(30)

print("myQueue:",end = "")
while not  myQueue.empty():
    print(myQueue.get(),end = " ")
print()

print("myStack:",end = "")
while not  myStack.empty():
    print(myStack.get(), end = " ")
print()