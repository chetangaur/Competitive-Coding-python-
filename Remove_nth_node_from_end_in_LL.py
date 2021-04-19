# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """temp=head      # sol 1
        n_temp=head
        l=0
        while(temp):
            l=l+1
            temp=temp.next
        index_to_remove=l-n
        if (index_to_remove==0):
            head=head.next
            return head
        else:
            count=0
            while(n_temp):
                if count==index_to_remove-1:
                    n_temp.next=n_temp.next.next
                    break
                n_temp=n_temp.next
                count=count+1
        return head"""
        temp=ListNode(0,head)              # soln 2
        slow=fast=temp
        for i in range(n):
            fast=fast.next
        while(fast.next):
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return temp.next
            
