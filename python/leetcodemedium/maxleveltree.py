from collections import deque
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.bfslist = deque()
        self.bfsdata = list()
        self.level = 0
        self.flag = 0
        self.sum = 0
    def bfs(self, root):
        self.bfslist.append(root)
        self.sum = root.data
        while len(self.bfslist)!=0:
            nodeData = self.bfslist.popleft()
            print(nodeData.data)
            if nodeData.left:
                self.bfslist.append(nodeData.left)
                if self.flag == 0:
                    self.level = self.level + 1
                    self.flag = 1
                localleft = nodeData.left.data
            else:
                localleft = 0
            if nodeData.right:
                self.bfslist.append(nodeData.right)
                if self.flag == 0:
                    self.level = self.level + 1
                    self.flag = 1
                localright = nodeData.right.data
            else:
                localright = 0
            if localleft + localright > self.sum:
                self.sum = localleft + localright
            print("sum:",self.sum)
            self.flag = 0
            print("level:",self.level)




        


t = Tree()
root = Node(1)
n1 = Node(7)
n2 = Node(0)
root.left = n1
root.right = n2
n3 = Node(7)
n1.left = n3
n4 = Node(-8)
n1.right = n4
t.bfs(root)


