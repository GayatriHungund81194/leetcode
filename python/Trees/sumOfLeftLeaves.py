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

    def isLeaf(self,root):

        if root is None:
            return False
        if root.left is None and root.right is None:
            print(root.data)
            return True
        return False
            
    def sumOfLeftLeaves(self,root):

        res = 0
        if root is not None:
            if self.isLeaf(root.left):
                res = res + root.left.data
            else:
                res = res + self.sumOfLeftLeaves(root.left)
            res = res+self.sumOfLeftLeaves(root.right)
        return res

root = Node(20) 
root.left = Node(9) 
root.right = Node(49) 
root.right.left = Node(23)         
root.right.right = Node(52) 
root.right.right.left = Node(50) 
root.left.left = Node(5) 
root.left.right = Node(12) 
root.left.right.right = Node(12) 
#root.printTree()
s=root.sumOfLeftLeaves(root)
print("Sum is:",s)