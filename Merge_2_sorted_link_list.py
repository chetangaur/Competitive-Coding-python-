# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:                     # if list1 is empty return list2
            return l2
        if l2==None:
            return l1
        current=dummy=ListNode(0)           # created a dummy node
        while(l1 and l2):                         # until both list become empty
            if l1.val <= l2.val:             # their are 2 pointer pointing towards head of list initially and 
                current.next=l1              # we need to compare them and every time take the smaller one and 
                l1=l1.next                   # put it into the new linklist with head is the dummy node
            else:                            # We do this iteration until all the element of any of list are covered 
                current.next=l2              
                l2=l2.next
            current=current.next
        if l1:                            # As intital l1 and l2 are also sorted so we can just append the another list to 
            current.next=l1               # the new link list
        if l2:
            current.next=l2                
        return dummy.next
