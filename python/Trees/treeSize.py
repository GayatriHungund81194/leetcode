class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data
        datalmax=0

    def insert(self, data):
        if self.data:
            if data< self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data=Node(data)
    
    def printree(self):
        if self.left:
            self.left.printree()
        print(self.data)
        if self.right:
            self.right.printree()

    def findSize(self,node):
        if (node == None):
            return 0
        else:
            return self.findSize(node.left)+1+self.findSize(node.right)
n
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printree()
max= root.findSize(root)
print("Exists:",max)

