# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val: #if l1 value > l2 value, then we swap them
            l1, l2 = l2, l1 
        l1.next = self.mergeTwoLists(l1.next, l2)    # always send the smallest value in the l1.next parameter
        return l1
