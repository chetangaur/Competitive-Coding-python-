# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val                # As we do not move back in singly linklist and also we do not traverse ll because we do not have head, so we put next value in given node
        node.next=node.next.next              # and then point it to next of next.
        
