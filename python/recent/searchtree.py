# class Node:
#     def __init__(self,data):
#         self.left = None
#         self.right = None
#         self.val = data

# class Tree:
    
#     def height(self,node):
#         if node is None:
#             return 0
#         lh = self.height(node.left)
#         rh = self.height(node.right)
#         if (lh > rh):
#             return lh + 1
#         else:
#             return rh + 1
    
#     def bfs(self,node):
#         temp = []
#         final = []
#         self.nodeque = list()
#         ht = self.height(node)
#         print(ht)
#         temp.append(node)
#         for i in range(ht-1):
#             print("Temp",temp)
#             while temp:
#                 node  = temp.pop(0)
#                 print("Node",node.val)
#                 if node.left:
#                     print("Data",node.left.val)
#                     self.nodeque.append(node.left)
#                 if node.right:
#                     print("Data right",node.right.val)
#                     self.nodeque.append(node.right)
#             temp = self.nodeque.copy()
#             final.append(temp.copy())
#             self.nodeque.clear()
#         height = ht - 2
#         summ = 0
#         arr = final[height]
#         for node in arr:
#             summ = summ + node.val
#         print(summ)


# n1=Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5
# t=  Tree()
# # res = t.search(n1,5)
# # print(res)
# t.bfs(n1)
stack = []
res = []
id = 0
while head:
    res.append(0)
    while stack and head.val > stack[-1][0]:
        _, ind = stack.pop()
        res[ind] = head.val
    stack.append((head.val,id))
    head = head.next
    id += 1