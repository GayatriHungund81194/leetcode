class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __inti__(self):
        self.head=None

    def traverseGetLength(self):
        temp = self.head
        count=0
        while temp!=None:
            print("",temp.data)
            temp=temp.next
            count = count + 1
        return count

    def insert(self,llist1, llist2):
        len1 = llist1.traverseGetLength()
        len2 = llist2.traverseGetLength()

        minlen = 0

        if len1 < len2:
            minlen = len1
        else:
            minlen = len2
        print("Len1",len1)
        print("len2",len2)
        print("",minlen)
        temp1 = llist1.head
        temp2 = llist2.head

        for x in range(2):
            if temp2.data >= temp1.data and minlen==len2:
                print("in if")
                node  = temp2
                node.next = temp1
                node = node.next
                temp1= temp1.next
            else:
                print("in else")
                node = temp1
                node.next = temp2.next
                temp2.next = node
                temp2 = temp2.next
                temp1=temp1.next
            
            
            

llist1 = linkedList()
llist2 = linkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(1)
n5 = Node(5)

llist1.head = n1
n1.next = n2
n2.next = n3

llist2.head = n4
n4.next = n5

llist1.traverseGetLength()
print("")
llist2.traverseGetLength()

llist1.insert(llist1,llist2)
print("After Inserting")

llist1.traverseGetLength()

