class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doubleLinkedList:

    def __init__(self):
        self.head = None
        
    def traverse(self):
        temp =self.head
        while temp!=None:
            print("",temp.data)
            temp = temp.next

    #insert at head
    def insertHead(self,node):
        temp = self.head
        temp.prev=node
        node.next=temp
        self.head=node

    #insert at end
    def insertEnd(self,node):
        temp = self.head
        while temp.next!=None:
            temp=temp.next
        temp.next = node
        node.prev = temp
    
    #insert after
    def insertAfter(self,node,k):
        temp = self.head
        count = 0
        while count!=k:
            temp= temp.next
            count=count+1
        node.next = temp.next
        temp.next.prev=node
        node.prev=temp
        temp.next=node

    #delete first
    def deleteFirst(self):
        temp=self.head
        temp.next.prev=None
        self.head=temp.next
        temp.next=None

    #delete last
    def deleteLast(self):
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.prev.next=None
        temp.prev=None

    def deleteAfter(self,k):
        temp  = self.head
        count = 0
        while k!=count:
            temp=temp.next
            count= count+1
        
        temp.next = temp.next.next
        #temp.next.prev=temp
        







llist = doubleLinkedList()
n1= Node("n1")
llist.head = n1
n2 = Node("n2")
n1.next=n2
n2.prev=n1
llist.traverse()
print("")
n3 = Node("n3")
llist.insertHead(n3)
llist.traverse()
print("")
n4 = Node("n4")
llist.insertEnd(n4)
llist.traverse()
print("")
n5 = Node("n5")
llist.insertAfter(n5,2)
llist.traverse()
print("")
llist.deleteFirst()
llist.traverse()
print("")
llist.deleteLast()
llist.traverse()
print("")
llist.deleteAfter(1)
llist.traverse()
print("")


