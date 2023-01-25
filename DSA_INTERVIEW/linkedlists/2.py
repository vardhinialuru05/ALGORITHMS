class Node:
    def __init__(self,data):
        self.value = data
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

def insertAtEnd(head, tail,value):
    newNode  = Node(value)
    if tail is None:
        head = tail = newNode
    else:
        tail.next = newNode
        tail = newNode
    return head

def printList(head):
    pointer = head
    while pointer is not None:
        print(pointer.value, "->" , end = " ")
        pointer = pointer.next
    print(None)

myList = LinkedList([])
printList(insertAtEnd(myList.head,myList.tail,6))