class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 
class Tree:
    def replace(self,key,node):
        if node is None:
            return
        if node.left:
            print("hey")
            self.replace(node.data,node.left)
            node.left.data = 2 * node.data + 1
        if node.right:
            self.replace(node.data,node.right)
            node.right.data = 2 * node.data + 2

    def delete(self,node,target):
        if node is not None:
            return
        node.left = self.delete(node.left,target)
        node.right = self.delete(node.right,target)
        if node.left is None and node.right is None and node.data==target:
            return None
        else:
            return node
        
    def deleteleaf(self,node):
        if node is None:
            return
        if node





t = Tree()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
t.replace(0,n1)
print(n1.left.data)
print(n1.right.data)
print(n2.left.data)
print(n2.right.data)
