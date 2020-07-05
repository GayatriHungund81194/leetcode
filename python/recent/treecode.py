class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 
class Tree:
    def __init__(self):
        self.paths = list()
        self.allpaths = list()
        self.maxi = 0
        self.leastnode = 9999
        self.lheightTree = 0
        self.lh = 0
        self.rh = 0
        self.currentCount = 0
        self.queue = []

    def postorder(self,node):
        if node is None:
            return 
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)

    def height(self,node):
        if node is None:
            return 0
        lh = self.height(node.left)
        rh = self.height(node.right)
        if (lh > rh):
            return lh + 1
        else:
            return rh + 1

    def constructFromPreorder(self,pre,size):
        root = Node(pre[0])
        s = list()
        s.append(root)
        i=1
        while i < size:
            prev = None
            while (s[-1]<pre[i] and len(s)>0):
                prev = s.pop()
            if prev is not None:
                prev.right = Node(pre[i])
                s.append(prev.right)
            else:
                temp = s[-1]
                temp.left = Node(temp)
                prev.left = Node(pre[i])
            i = i + 1
        return root

        # while(i<size):
        #     temp = None
        #     while(len(s)>0 and pre[i]>s[-1].data):
        #         temp = s.pop()
            
        #     if (temp!=None):
        #         temp.right = Node(pre[i])
        #         s.append(temp.right)
        #     else:
        #         temp = s[-1]
        #         temp.left = Node(temp)
        #         s.append(temp.left) 

    def findAllPaths(self,node):
        if node is None:
            return
        self.paths.append(node.data)
        self.findAllPaths(node.left)
        if (node.left == None and node.right==None):
            print(self.paths)
        self.findAllPaths(node.right)
        self.paths.pop()

    def maximumDepth(self,node):
        if node is None:
            return
        self.paths.append(node.data)
        self.maximumDepth(node.left)
        if (node.left is None and node.right is None):
            if (self.maxi < len(self.paths)):
                self.maxi = len(self.paths)
        self.maximumDepth(node.right)
        self.paths.pop()
    
    def findMaxDepth(self,node):
        self.maximumDepth(node)
        print("Maximum Depth:",self.maxi)

    def findLeastNode(self,node):
        if node is None:
            return
        self.findLeastNode(node.left)
        if (node.data < self.leastnode):
            self.leastnode = node.data
            print(self.leastnode)
        self.findLeastNode(node.right)

    def searchNodeInBST(self,node,data):
        if node is None:
            return
        while (node.data!=data):
            if data < node.data:
                node = node.left
                print("Node data",node.data)
            else:
                node = node.right
                print("Node data right",node.data)

    def findPrevNode(self,node,data):
        if node is None:
            return
        while (node.data!=data and node is not None):
            if data < node.data:
                self.allpaths.append(node.data)
                node = node.left
            else:
                node = node.right

    def findInorderSuccessor(self,root,node,data):
        if node.right is not None:
            self.findLeastNode(node.right)
            print("Inorder Successor:",self.leastnode)
        elif node.right is None:
            self.findPrevNode(root,data)
            print("Inorder Prev:",self.allpaths[-1])

    def nNodeInorder(self,node,count):
        if node is None:
            return
        if count>= self.currentCount:
            self.nNodeInorder(node.left,count)
            self.currentCount = self.currentCount + 1
            if (self.currentCount == count):
                print("Nth node",node.data)
            self.nNodeInorder(node.right,count)

    def bfs(self,node):
        if not node:
            return None
        self.queue.append(node)
        while (len(self.queue)!=0):
            nod = self.queue.pop(0)
            print("",nod.data)
            if nod.left:
                self.queue.append(nod.left)
            if nod.right:
                self.queue.append(nod.right)

    def averageOfLevels(self, root):
        que = list()
        temp = list()
        avglist = list()
        summ = 0
        if root is None:
            return
        que.append(root)
        avglist.append(root.data)
        while len(que)!=0:
            summ = 0
            temp = list()
            count = 0
            while (len(que)!=0):
                node = que.pop(0)
                summ = summ + node.data
                count = count + 1
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            que = temp
            avglist.append(summ/count)
            # if len(que)==0 and len(temp)!=0:
            #     for elem in temp:
            #         summ = summ + elem.data
            #     avg = summ/len(temp)
            #     print("Temp",temp)
            #     avglist.append(avg)
            #     que = que + temp
            #     temp.clear()

    def lowestCommon(self,node,val):
        arr = list()
        arr.append(node.data)
        if node is None:
            return
        while(node.data!=val):
            if val < node.data:
                node = node.left
                arr.append(node.data)
            else:
                node = node.right
                arr.append(node.data)
        print(arr)

n1 = Node(20)
n2 = Node(8)
n3 = Node(22)
n4 = Node(4)
n5 = Node(12)
n6 = Node(10)
n7 = Node(14)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n6
n5.right = n7
t = Tree()
#t.postorder(n1)
# t.findAllPaths(n1)
# print(t.paths)
#t.findMaxDepth(n1)
#t.findLeastNode(n1)
#print(t.leastnode)
#t.findInorderSuccessor(n1,n7,14)
#t.findInorderSuccessor(n1)
#t.nNodeInorder(n1,4)
#t.bfs(n1)
#t.averageOfLevels(n1)
#t.lowestCommon(n1,14)
t.height(n1)