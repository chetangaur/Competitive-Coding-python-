# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """temp= head             # method 1 
        length=0
        while(temp):
            length=length+1
            temp=temp.next
        ll_length=length
        ran=(int(ll_length/2))
        temp= head
        for i in range(ran):
            temp=temp.next
        return temp"""
        slow=head                  # method 2 simultaneously move 2 pointers
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow
                
                
