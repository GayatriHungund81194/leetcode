class Node:
    def __init__(self, data):
        self.left =  None
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
        print("",self.data)
        if self.right:
            self.right.printTree()

    def height(self,node): 
        if node is None: 
            return 0 
        else:
            lht = self.height(node.left)+1
        
            rht = self.height(node.right)+1
        return max(lht,rht)

    def printlvldata(self,node,level):
        if node  is None:
            return
        if  level  == 1:
            print(node.data)
        elif level >1:
            self.printlvldata(node.left,level-1)
            self.printlvldata(node.right,level-1)
        
        
    def bfs(self,root):
        h = self.height(root)
        for i in range(1,h+1):
            self.printlvldata(root,i)

root = Node(3)
root.insert(1)
root.insert(2)
root.insert(4)
root.printTree()
print("")
ht= root.height(root)

root.bfs(root)