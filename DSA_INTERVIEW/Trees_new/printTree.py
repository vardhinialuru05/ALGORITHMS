from treeNode import Node
 
a = Node(1)
b = Node(2)
c = Node(3)

a.left = b
a.right = c

def printTree(root):
    if root is None:
        return []

    return printTree(root.left) + [root.val] + printTree(root.right)

print(printTree(a))