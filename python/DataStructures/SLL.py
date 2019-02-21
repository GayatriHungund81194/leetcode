class Node:
    def __init__(self, nodeData):
        self.nodeData = nodeData
        self.next=None
        
class singleLinkedList:
    def __init__(self):
        self.head = None

    #print list
    def traverse(self):
        temp = self.head
        while temp!=None:
            print("",temp.nodeData)
            temp = temp.next

    #insert at head
    def insertHead(self, node):
        node.next=self.head
        self.head=node

    #insert at end
    def inserAtEnd(self,node):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=node

    #insert at middle
    def insertafter(self, node,k):
        temp=self.head
        count =0
        while count!=k:
            temp=temp.next
            count = count+1
        node.next = temp.next
        temp.next=node

    #remove last
    def delLast(self):
        temp = self.head
        while temp.next.next!=None:
            temp = temp.next
        temp.next=None

    #delete head
    def delHead(self):
        temp = self.head
        self.head=temp.next

    #delete middle
    def delafter(self,k):
        count=0
        temp = self.head
        while count!=k:
            count = count+1
            temp=temp.next
        temp.next=temp.next.next
        


llist = singleLinkedList()
llist.head=Node("1")
n1 = Node("2")
llist.head.next=n1
llist.traverse()
print("")
n2 = Node("0")
llist.insertHead(n2)
llist.traverse()
print("")
n3 = Node("3")
llist.inserAtEnd(n3)
llist.traverse()
print("")
n4 = Node("4")
llist.insertafter(n4,2)
llist.traverse()
print("")
llist.delLast()
llist.traverse()
print("")
llist.delHead()
llist.traverse()
print("")
llist.delafter(1)
llist.traverse()
print("")
