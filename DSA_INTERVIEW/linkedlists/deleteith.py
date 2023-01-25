from LL import LinkedList, Node
def delete(head,index):
    count = 0
    pointer = head
    if index == 0:
        head = head.next
    else:
        while count < index:
            before = pointer
            pointer = pointer.next
            count += 1
        before.next = pointer.next
    return head

def printList(head):
    pointer = head
    while pointer is not None:
        print(pointer.data , "->" , end = " ")
        pointer = pointer.next
    print(None)

myList = LinkedList([1, 2, 3, 4, 5])
printList(delete(myList.head,0))