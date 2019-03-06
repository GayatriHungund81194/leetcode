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

    def search(self,node,data):
        if (node == None):
            return 0
        elif node.data == data:
            return 1
        else:
            
            srchldata = self.search(node.left,data)
        if (srchldata==0):
            srrchrdata = self.search(node.right,data)
        return srchldata or srrchrdata
            

        
        


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printree()
max= root.search(root,14)
print("Exists:",max)

