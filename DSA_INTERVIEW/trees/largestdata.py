from bt import Node

def inputTree():
    nodeData = int(input())
    
    if nodeData == -1:
        return
    newNode = Node(nodeData)
    newNode.left = inputTree()
    newNode.right = inputTree()

    return newNode

def largest(root):
    if root is None:
        return -10**9
    max = root.val
    left = largest(root.left)
    right = largest(root.right)

    if left > max:
        max = left
    if right > max:
        max = right
    
    return max
    
root = inputTree()
print("max value"  ":", largest(root))