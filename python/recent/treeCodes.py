class Node:
    def __init__(self, val):
        self.left=None
        self.right=None
        self.val=val

class Tree:
    def __init__(self):
        self.arr = list()
        self.size = 0
        self.count=  0
        self.queue = list()
        self.arr1 = list()
        self.arr2 = list()
        self.arr3 = list()
        self.arr4 = list()

    # def preorder(self,root):
    #     if root is not None:
    #         print(root.data)
    #         self.preorder(root.left)
    #         self.preorder(root.right)

    def nodeWithMinBST(self,root):
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr.data
        
    def nodeWithMaxBST(self,root):
        curr = root
        while curr.right is not None:
            curr = curr.right
        return curr.data

    # def inorder(self,root):
    #     if root is not None:
    #         self.inorder(root.left)
    #         self.arr.append(root.data)
    #         self.inorder(root.right)
    #     print("Arr:",self.arr)
    #     a = self.arr
    #     b = sorted(a)
    #     print("B:",b)
    #     swap = 0
    #     for i in range(len(b)):
    #         if (a[i]!=b[i]):
    #             index = self.findIndex(a,b[i])
    #             swap = swap + 1
    #             a[i],a[index] = a[index],a[i]
    #         print(swap)

    def findIndex(self,arr,b):
        for i in range(len(arr)):
            if (b==arr[i]):
                return i

    def dfs(self,root):
        if root is not None:
            self.dfs(root.left)
            self.count = self.count + 1
            self.dfs(root.right)
            print(self.count)

    def height(self,root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height,right_height)

    def preorder(self,root,arr):
        if root:
            arr.append(root.val)
            if (root.left is None):
                arr.append("lnull")
            if (root.right is None):
                arr.append("rnull")
            self.preorder(root.left,arr)
            self.preorder(root.right,arr)
    
    def postorder(self,root,arr):
        if root:
            self.postorder(root.left,arr)
            self.postorder(root.right,arr)
            arr.append(root.val)
            if (root.left is None):
                arr.append("lnull")
            if (root.right is None):
                arr.append("rnull")

    def checkSubtree(self,n1,n2):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False
        l = self.checkSubtree(n1.left, n2.left)
        r = self.checkSubtree(n1.right, n2.right)
        if (l and r and n1.val==n2.val):
            return True
        else: 
            return False
        
    def heightNode(self,start,node,h):
        if node is None:
            return 0
        if node == start:
            return h
        lvl = self.heightNode(start.left,node,h+1)
        if (lvl !=0):
            return lvl
        return self.heightNode(start.right,node,h+1)


root = Node(3)
n1 = Node(4)
n2 = Node(5)
n3 = Node(1)
n4 = Node(2)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
t = Tree()

root1 = Node(4)
nn = Node(1)
root1.left = (nn)
# t.preorder(root)
# b = t.nodeWithMinBST(root)
# t.inorder(root)
# t.dfs(root)
# t.preorder(root,t.arr1)
# t.preorder(root1,t.arr2)
# t.postorder(root,t.arr3)
# t.postorder(root1,t.arr4)
#t.inorder(root1)
# print(t.arr1)
# print(t.arr2)
# print(t.arr3)
# print(t.arr4)
#beep = t.checkSubtree(root.left,root1)
tt = t.heightNode(root,n1,1)
print(tt)