from bt import Node

def printTree(root):
    if root is None:
        return
    print(root.val, ":",end = " ")

    if root.left is not None:
        print(root.left.val ,end = " ")
    if root.right is not None:
        print(root.right.val,end = " ")
    
    print()
    
    printTree(root.left)
    printTree(root.right)

def inputTree():
    nodeData = int(input())
    
    if nodeData == -1:
        return
    newNode = Node(nodeData)
    newNode.left = inputTree()
    newNode.right = inputTree()

    return newNode

root = inputTree()
printTree(root)


