from LL import LinkedList, Node
def delete(head,index):
    if index == 0:
        return head.next
    head.next = delete(head.next,index-1)    
    return head

def printList(head):
    pointer = head
    while pointer is not None:
        print(pointer.data , "->" , end = " ")
        pointer = pointer.next
    print(None)

myList = LinkedList([1, 2, 3, 4, 5])
printList(delete(myList.head,0))