class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data: 
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right = Node(data)
            else:
                self.data = Node(data)
        
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    
    def deleteTree(self):
        if self.left:
            self.left.deleteTree()
        self.data = None
        if self.right:
            self.right.deleteTree()

    def sizeBinTr(self):
        leftSize = self.left.sizeBinTr() if self.left else 0
        rightSize = self.right.sizeBinTr() if self.right else 0
        return leftSize + 1 + rightSize
        




root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()
root.deleteTree()
root.printTree()
size=root.sizeBinTr()
print("Size:",size)