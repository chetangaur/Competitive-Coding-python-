"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(0)
        temp=dummy
        summ=0
        while(l1 or l2 or summ):
            #summ=0
            if(l1):
                summ=summ+l1.val
                l1=l1.next
            if(l2):
                summ=summ+l2.val
                l2=l2.next
            temp.next=ListNode(summ%10)
            temp=temp.next
            summ=summ//10
        return dummy.next
