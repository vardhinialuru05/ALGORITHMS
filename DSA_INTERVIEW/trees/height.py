from bt import Node

def inputTree():
    nodeData = int(input())
    
    if nodeData == -1:
        return
    newNode = Node(nodeData)
    newNode.left = inputTree()
    newNode.right = inputTree()

    return newNode

def depth(root):
    if root is None:
        return 0
    return 1 + max(depth(root.left),depth(root.right))

root = inputTree()
print("height"  ":", depth(root))