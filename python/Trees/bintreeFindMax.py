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

    def givMax(self,node):
        if (node == None):
            return -99999
        res = node.data
        lmax = self.givMax(node.left)
        rmax = self.givMax(node.right)
        if (lmax > res):
            res = lmax
        if (rmax > res):
            res = rmax
        return res
            

        
        


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printree()
max= root.givMax(root)
print("Max:",max)

