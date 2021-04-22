# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''temp=head                           #    Just put temp data in a list and every time check if
        l=[]                                    # temp.next present in list then their must me a cycle
        while(temp):
            if temp not in l:
                l.append(temp)
                temp=temp.next
            else:
                return True
        return False'''
        if head==None or head.next==None:            # Using slow and fast pointer
            return False                             # if slow and fast pointer conside that cycle exits
        slow=fast=head
        while(fast.next and fast.next.next):         # optimized soln
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False
        

        
