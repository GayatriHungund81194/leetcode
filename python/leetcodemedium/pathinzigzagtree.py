class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.path = list()

    def inOrder(self,root):
        if root is None:
            return None
        
        self.inOrder(root.left)
        self.inOrder(root.right)
        print(root.data)

def allpaths(node,pathArr,index,key):
    if node is None:
        return None
    if (len(pathArr)>index):
        pathArr[index] = node.data
    else:
        pathArr.append(node.data)
    index = index + 1
    if node.data==key:
        printArray(pathArr,index)
    allpaths(node.left,pathArr,index,key)
    allpaths(node.right,pathArr,index,key)

def printArray(ints, len): 
    for i in ints[0 : len]: 
        print(i," ",end="") 
    print() 

t = Tree()
root = Node(10)
n1 = Node(8)
n2 = Node(2)
root.left = n1
root.right = n2
n3 = Node(3)
n1.left = n3
n4 = Node(5)
n1.right = n4
n5 = Node(4)
n2.left = n5
allpaths(root,[],0,4)


