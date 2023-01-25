#we have to check the balance factor
from bt import Node

def inputTree():
    nodeData = int(input())
    
    if nodeData == -1:
        return
    newNode = Node(nodeData)
    newNode.left = inputTree()
    newNode.right = inputTree()

    return newNode

def helper(root):
    if root is None:
        return   0, True
    leftHeight , leftStatus = helper(root.left)
    rightHeight , rightStatus = helper(root.right)

    balanceFactor = abs(leftHeight - rightHeight)
    height = 1 + max(leftHeight,rightHeight)

    if leftStatus is False or rightStatus is False:
        return height,False
    if balanceFactor <= 1:
        return height, True
    else:
        return height,False

def balance(root):
    garbage, result = helper(root)
    return result

root = inputTree()
print(balance(root))