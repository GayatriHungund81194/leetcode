import queue

class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 

def inorderTrav(node):
    if (node == None):
        return
    inorderTrav(node.left)
    print("Node-> left:",node.val)
    inorderTrav(node.right)
    
def bfsQueue(node):
    bfsq = []
    bfsq.append(node)
    count = 1
    count1 = 0
    count2 = 0

    while(len(bfsq)>0):
        print(bfsq[0].val)
        node = bfsq.pop(0)

        if (node.left != None):
            bfsq.append(node.left)
            count = count + 1
        
        if (node.right!= None):
            bfsq.append(node.right)
        
def printAllLeftNodes(node):
    leftview = []
    count = 0
    if (count == 0):
        leftview.append(node)
        print("root:",leftview[0].val)
        count = count +1 

    while(len(leftview)>0):
        node = leftview.pop(0)
        if (node.left != None):
            print("Left:",node.left.val)

        if (node.left != None):
            leftview.append(node.left)
        
        if (node.right != None):
            leftview.append(node.right)
    
def rightView(node):
    nodeList = []
    nodes = []
    nodereverse = []
    tracklist = []
    count = 1
    nodeList.append(node)
    nodereverse.append(node.val)
    tracklist.append(node)

    print(node.val)

    while (len(nodeList)>0):
        if (len(tracklist) == 0):
            tracklist = nodeList[:]
        node = nodeList.pop(0)
        print("count",count)
        print ("Nodereverse List:",nodereverse)
        del tracklist[-1]
        value = nodereverse[-1]
        n = nodereverse.pop(0)
        if (value not in nodes and len(tracklist) == 1):
            nodes.append(value)
        count = count - 1
        if (node.left != None):
            nodeList.append(node.left)
            nodereverse.append(node.left.val)
            
            count = count + 1
        
        if (node.right != None):
            nodeList.append(node.right)
            nodereverse.append(node.right.val)
            
            count = count + 1
        print("Nodes:",nodes)

def view(node):
    que = []
    height = 0
    if (node == None):
        return None
    que.append(node)
    height = 0 

    while(True):
        nodecount = len(que)
        print("Node count:",nodecount)
        if (nodecount == None):
            return height
        
        height = height + 1
        
        while (nodecount > 0):
            node = que.pop(0)
            if (node.left != None):
                que.append(node)
            if (node.right != None):
                que.append(node)
            nodecount = nodecount - 1
    print(height)

def rangeSumBST(node, L,R):
    sum = 0
    if (root == None):
        return 
    rangeSumBST(root.left,L,R)
    n = root.val
    rangeSumBST(root.right,L,R)
    if(n>=L or n<=R):
        sum = sum + n
        print(sum)
        return sum

# create root 
root = Node(1) 
root.left	 = Node(2) 
root.right	 = Node(3)

root.left.left = Node(4)

root.left.right = Node(5)
root.right.right = Node(4)

#inorderTrav(root)
#bfsQueue(root)
#printAllLeftNodes(root)
#rightView(root)
#view(root)
rangeSumBST(root,2,4)

