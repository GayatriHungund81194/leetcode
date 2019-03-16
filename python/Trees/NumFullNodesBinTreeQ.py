import collections
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
    
    def numfullnodes(self,node):
        count =0
        queue = []
        queue.append(node)
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is not None and node.right is not None:
                count = count+1
                print(count)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return count

        



root = Node(3)
root.insert(1)
root.insert(2)
root.insert(4)
root.printTree()
print("")
root.numfullnodes(root)
