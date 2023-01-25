from bt import Node

def inputTree():
    nodeData = int(input())
    
    if nodeData == -1:
        return
    newNode = Node(nodeData)
    newNode.left = inputTree()
    newNode.right = inputTree()

    return newNode


def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)

root = inputTree()
print("no of nodes"  ":", count(root))
