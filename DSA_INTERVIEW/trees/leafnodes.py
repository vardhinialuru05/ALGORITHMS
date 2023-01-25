from ast import Not
from bt import Node

def inputTree():
    nodeData = int(input())
    
    if nodeData == -1:
        return
    newNode = Node(nodeData)
    newNode.left = inputTree()
    newNode.right = inputTree()

    return newNode

def leaf(root):
    if root is None:
        return
    if root is Not -1:
        return 1 + leaf(root.left) + leaf(root.right)

root = inputTree()
print("result"  ":", leaf(root))