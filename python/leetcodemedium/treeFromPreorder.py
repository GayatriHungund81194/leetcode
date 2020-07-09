class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

preorder  =[8,5,1,7,10,12]
root = TreeNode(preorder[0])
stack = [root,]

for i in range(1,len(preorder)):
    current,child = stack[-1],TreeNode(preorder[i])
    
    while stack and stack[-1].val < child.val:
        current = stack.pop()
        
    if current.val < child.val:
        current.right = child
    else:
        current.left = child
    stack.append(child)