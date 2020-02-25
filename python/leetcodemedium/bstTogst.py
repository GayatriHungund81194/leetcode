class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.sum = 0
    def inOrder(self,root):
        if root is None:
            return None
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)

    def reverseInorder(self,root):
        if root is None:
            return None
        self.sum = self.sum + root.data
        self.reverseInorder(root.right)
        print(root.data)
        self.reverseInorder(root.left)
        print("Sum:",self.sum)

t = Tree()
root = Node(4)
n1 = Node(1)
n2 = Node(6)
root.left = n1
root.right = n2
n3 = Node(0)
n1.left = n3
n4 = Node(2)
n1.right = n4
n5 = Node(3)
n4.right = n5
n6 = Node(5)

t.reverseInorder(root)



