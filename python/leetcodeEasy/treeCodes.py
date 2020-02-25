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

    def preOrder(self,root):
        if root is None:
            return None
        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return None
        self.preOrder(root.left)
        self.preOrder(root.right)
        print(root.data)

    def dfs(self,root,left,right):
        if root is None:
            return None
        if root.data > left and root.data < right:
            self.ans = self.ans + root.data
            print(self.ans)
        if left < root.data:
            self.dfs(root.left,left,right)
        if left > root.data:
            self.dfs(root.right,left,right)

    def rangeSum(self, root,left,right):
        def dfs(root):
            if root is None:
                return None
            if left <=  root.data <= right:
                self.ans = self.ans + root.data
                print(self.ans)
            if left < root.data:
                dfs(root.left)
            if left > root.data:
                dfs(root.right)
        self.ans = 0
        dfs(root)
        return self.ans


        


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


