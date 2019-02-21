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

    def getLength(self,list):
        temp = list.head
        len=0
        while temp!=None:
            len = len +1 
            temp = temp.next
        return len
        
    def insertatBeginningEven(self,list):
        len = self.getLength(list)
        print("Length",len)
        temp = self.head
        for x in range(3):
            while temp.next.nodeData%2!=0:
                temp = temp.next
            node = temp.next
            node2 = node.next
            temp.next=node2
            node.next = self.head
            self.head = node
        




llist = singleLinkedList()
llist.head=Node(1)
n1 = Node(2)
llist.head.next=n1
n2 = Node(3)
n1.next= n2
n3 = Node(4)
n2.next= n3
n4 = Node(6)
n3.next= n4
llist.traverse()
print("")
llist.insertatBeginningEven(llist)
llist.traverse()
print("")