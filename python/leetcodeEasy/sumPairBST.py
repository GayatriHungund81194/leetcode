class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.nodeList = list()
    def inOrder(self,root):
        if root is None:
            return None
        self.inOrder(root.left)
        print(root.data)
        self.nodeList.append(root.data)
        print(self.nodeList)
        self.inOrder(root.right)

    def getMaxSumPair(self,nodeList):
        return nodeList[-1] + nodeList[-2]


        
        


t = Tree()
root = Node(15)
n1 = Node(10)
n2 = Node(20)
root.left = n1
root.right = n2
n3 = Node(8)
n1.left = n3
n4 = Node(12)
n1.right = n4
t.inOrder(root)
maxSum = t.getMaxSumPair(t.nodeList)
print(maxSum)
# t.preOrder(root)
# t.postOrder(root)
# s = t.rangeSum(root,1,4)
# print("Sum:",s)


