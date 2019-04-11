class Node:
    def __init__(self, data):
        self.left =  None
        self.right = None
        self.data = data
    
    def insert(self,data):
        if self.data: 
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = Node(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print("",self.data)
        if self.right:
            self.right.printTree()

    def traverseLeft(self):
        if self.left:
            self.left.traverseLeft()
        print(self.data)

    def traverseRight(self):
        if self.right:
            self.right.traverseRight()
        print(self.data)    




root = Node(4)
root.insert(3)
root.insert(2)
root.insert(5)
root.insert(1)
root.insert(6)
#root.printTree()
root.traverseRight()