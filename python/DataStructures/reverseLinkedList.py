class Node:
    def __init__(self,nodeData):
        self.data = nodeData
        self.next = None

class linkedList:
    def __init__(self):
       self.head=None

    def traverse(self):
        temp = self.head
        while temp!=None:
            print("",temp.data)
            temp=temp.next

    def reverse(self):
        prev = None
        current = self.head
        nextNode = self.head

        while current!=None:
            nextNode = current.next
            current.next=prev
            prev = current
            current=nextNode
        self.head=prev




llist = linkedList()
n1 = Node("n1")
llist.head = n1
n2 = Node("n2")
n1.next=n2
n3 = Node("n3")
n2.next=n3
llist.traverse()
print("")
llist.reverse()
llist.traverse()