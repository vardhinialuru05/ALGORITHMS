class Node:
    def __init__(self,data = None):
        self.val = data
        self.right = None
        self.left = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.left = node2
node1.right = node3
