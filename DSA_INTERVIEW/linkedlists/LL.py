class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, arr):
        self.head = None
        self.tail = None
        if type(arr) is list:
            for ele in arr:
                newNode = Node(ele)
                if self.head is None:
                    self.head = self.tail = newNode
                else:
                    self.tail.next = newNode
                    self.tail = newNode
