class Node:
    def __init__(self,nodeData):
        self.nodeData=nodeData
        self.next = None
    
class circularLinkedList:
    def __init__(self):
        self.head = None
        #sself.head.next = self.head

    def traverse(self):
        temp = self.head
        while True:
            print("",temp.nodeData)
            temp= temp.next
            if temp==self.head:
                break
    
    def insertHead(self,node):
        temp = self.head
        node.next=temp
        while temp.next!=self.head:
            temp = temp.next
        temp.next=node
        self.head=node


llist  = circularLinkedList()

llist.head = Node("n1")
n2 = Node("n2")
llist.head.next=n2
n2.next=llist.head
llist.traverse()
print("")
n3 = Node("n3")
llist.insertHead(n3)
llist.traverse()
print("")