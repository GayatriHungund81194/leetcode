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

    def leftLeavesSum(self):
            if self.left is None and self.right is None:
                print(self.data)
            else:
                self.left.leftLeavesSum()
            self.right.left

    

root = Node(10)
root.insert(7)
root.insert(5)
root.insert(1)
root.insert(6)
root.insert(11)
root.insert(9)
#root.printTree()
root.leftLeavesSum()