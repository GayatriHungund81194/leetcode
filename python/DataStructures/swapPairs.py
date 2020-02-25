#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return
        if head.next is None:
            return head
        n1 = self.swapPairs(head.next.next)
        temp = head
        head = head.next
        head.next = temp
        head.next.next = n1
        print("N1:",n1.val)
        return head

head=ListNode(1)
head1=head
head2=ListNode(2)
head3=ListNode(3)
head4=ListNode(4)
head1.next=head2
head2.next=head3
head3.next=head4
s=Solution()
s.swapPairs(head1)