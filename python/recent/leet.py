class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 
class Tree:
    def __init__(self):
        self.paths = list()
        self.ll = list()
    
    def find(self,root):
        count = 0
        while count!=2:
            self.findleaves(root)
            self.ll.append(self.paths)
            self.paths.clear()
            count = count + 1
        print(self.paths)

    def findleaves(self,root):
        if root is None:
            return
        if root.left is None and root.right is None:
            print(self.paths)
            self.paths.append(root.data)
            return None
        root.left = self.findleaves(root.left)
        root.right = self.findleaves(root.right)
        return root


    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
t = Tree()
n1.left = n2
n1.right = n3
n2.left = n4
t.postorder(n1)
t.find(n1)
print("Paths",t.paths)
t.postorder(n1)