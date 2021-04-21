# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """tempA=headA                  
        tempB=headB                     # This is the brute force solution.
        while(tempA):
            while(tempB):
                if tempA==tempB:
                    return tempA
                tempB=tempB.next
            tempB=headB
            tempA=tempA.next
        return None"""
        """tempA=headA               # In optimal method 
        tempB=headB
        len1=0
        len2=0
        while(tempA):
            tempA=tempA.next
            len1=len1+1
        while(tempB):
            tempB=tempB.next
            len2=len2+1
        tempA=headA
        tempB=headB
        Maxx=max(len1,len2)
        Minn=min(len1,len2)
        
        
        
        for i in range(Maxx+1):                    # we traverse through the maximum length and if list points to null then assign it to 
            if tempA:                              # first element of another list
                tempA=tempA.next                   # so at the end both list are align
            else:
                tempA=headB
            if tempB:
                tempB=tempB.next
            else:
                tempB=headA
        while(tempA):                              # now we can traverse through the list and compare heads simultaneously.
            
            if tempA==tempB:
                return tempA
            else:
                tempA=tempA.next
                tempB=tempB.next
        return None"""
        tempA=headA                                   # same approach as above just code optimize
        tempB=headB
        while(tempA!=tempB):
            if tempA:
                tempA=tempA.next
            else:
                tempA=headB
            if tempB:
                tempB=tempB.next
            else:
                tempB=headA
        return tempA
    
                
            
        
            
                
        
