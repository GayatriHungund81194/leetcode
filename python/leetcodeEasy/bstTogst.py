class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def inOrder(self,root):
        if root is None:
            return None
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)

t = Tree()
root = Node(1)
n1 = Node(2)
n2 = Node(3)
root.left = n1
root.right = n2
n3 = Node(4)
n1.left = n3
n4 = Node(5)
n1.right = n4
# t.inOrder(root)
# t.preOrder(root)
# t.postOrder(root)
# s = t.rangeSum(root,1,4)
# print("Sum:",s)
t.printPath(root)


