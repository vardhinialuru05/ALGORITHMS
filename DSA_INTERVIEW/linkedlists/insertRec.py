from LL import LinkedList, Node
def insert(head,index,value):
    if index == 0:
        newNode  = Node(value)
        newNode.next = head
        return newNode
    smallHead = insert(head.next,index-1,value)
    head.next = smallHead
    return head

def printList(head):
    pointer = head
    while pointer is not None:
        print(pointer.data , "->" , end = " ")
        pointer = pointer.next
    print(None)

myList = LinkedList([1, 2, 3, 4, 5])
printList(insert(myList.head,5,6))

        
