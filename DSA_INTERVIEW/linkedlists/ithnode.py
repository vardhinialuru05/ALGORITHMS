from LL import LinkedList, Node
def printIthNode(head, index):
    count = 0
    pointer = head
    while count < index:
        pointer = pointer.next
        count += 1
    print("Value at %dth node: " % (index), pointer.data)
myList = LinkedList([1, 2, 3, 4, 5])

printIthNode(myList.head, 0)