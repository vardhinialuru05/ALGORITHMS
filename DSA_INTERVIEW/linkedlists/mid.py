from LL import LinkedList, Node

def length(head):
    pointer = head
    count = 0
    while pointer is not None:
        count += 1
        pointer = pointer.next
    return count

def mid(head):
    len = length(head)
    if len % 2 == 0: 
        len = (len - 1)//2
    else:
        len = len//2
    pointer = head
    for i in range(len):
        pointer = pointer.next
    return pointer.data

myList = LinkedList([1, 2, 3, 4, 5,6])
print(mid(myList.head))