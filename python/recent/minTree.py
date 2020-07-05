#1 right child 3 and left child of 3 as 2
import numpy as np
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.arr = list()


    def minDiffTree(self,root):
        self.min_val  = float('inf')
        self.vals = []

        def search(node):
            if node.left:
                self.vals.append(node.left.val)
                search(node.left)
            if node.right:
                self.vals.append(node.right.val)
                search(node.right)
    
        search(root)

        def diff(vals):
            sorted_list = sorted(vals)
            for i in range(len(sorted_list)-1):
                if (np.abs(sorted_list[i+1]-sorted_list[i])<self.min_val):
                    self.min_val = np.abs(sorted_list[i+1]-sorted_list[i])
        
        diff(self.vals)

        return self.min_val


t = Tree()
n1 = Node(1)
n2 = Node(2)
n3  = Node(3)
n1.right = n3
n3.left = n2
minnum = t.minDiffTree(n1)
print(minnum)






