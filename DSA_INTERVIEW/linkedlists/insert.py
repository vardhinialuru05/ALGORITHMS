from LL import LinkedList, Node

def insert(head,index,value):
    newNode  = Node(value)

    if index == 0:
        newNode.next = head
        head = newNode
    else:
        count = 0
        pointer = head
        while count < index-1:
            pointer = pointer.next
            count += 1
        newNode.next = pointer.next
        pointer.next = newNode
    return head

def printList(head):
    pointer = head
    while pointer is not None:
        print(pointer.data , "->" , end = " ")
        pointer = pointer.next
    print(None)

myList = LinkedList([1, 2, 3, 4, 5])
printList(myList.head)
printList(insert(myList.head,5,6))
