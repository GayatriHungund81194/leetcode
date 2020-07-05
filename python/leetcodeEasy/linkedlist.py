class Node:
    def __init__(self,nodeData):
        self.nodeData=nodeData
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def traverse(self):
        printv = self.head
        while printv!=None:
            print("",printv.nodeData)
            printv = printv.next
    
    def atBeginning(self,newdata):
        newNode = Node(newdata)
        newNode.next=self.head
        self.head=newNode

    def atEnd(self,newData):
        newNode = Node(newData)
        if self.head is None:
            return 
        lastNode = self.head
        while lastNode.next!=None:
            lastNode=lastNode.next
        lastNode.next=newNode
    
    def inMid(self,node,newData):
        newNode = Node(newData)
        newNode.next=node.next
        node.next = newNode

    def removeHead(self):
        node = self.head
        self.head=None
        node.next=self.head

    def removeLast(self):
        node = self.head
        while node!=None:
            node = node.next
        node.next=None

list = LinkedList()
list.head=Node("Hi")
n1 = Node("This")
n2 = Node("is a")
list.head.next=n1
n1.next=n2
list.traverse()
list.atBeginning("Inserting at beginning")
list.traverse()
list.atEnd("End")
list.traverse()
list.inMid(n1,"dfsdf")
list.traverse()
list.removeHead()
list.traverse()
list.removeLast()
list.traverse()