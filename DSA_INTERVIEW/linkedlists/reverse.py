from LL import LinkedList, Node

# def reverse(node):
#     if node.next == None:
#         return node
#     pointer = reverse(node.next)
#     node.next.next = node
#     node.next = None
#     return pointer
def printList(head):
    pointer = head
    while pointer is not None:
        print(pointer.data , "->" , end = " ")
        pointer = pointer.next
    print(None)

# without recursion:

graph = {
    'A': ['B', 'C'],
    'B': ['D','E'],
    "C": ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F':[]
}

path = list()

def DFS(currentNode,destination,graph,maxDepth,curList):
    print("Checking for destination",currentNode)
    curList.append(currentNode)
    if currentNode==destination:
        return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS(node,destination,graph,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False

def iterativeDDFS(currentNode,destination,graph,maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode,destination,graph,i,curList):
            return True
    return False

if not iterativeDDFS('A','E',graph,4):
    print("Path is not available")
else:
    print("A path exists")
    print(path.pop())