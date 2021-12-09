class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1=len(nums1)
        l2=len(nums2)
        # res=[]                              # soln1 
        # if l2<=l1:
        #     for i in range(l2):
        #         if nums2[i] in nums1:
        #             res.append(nums2[i])
        #             nums1.remove(nums2[i])
        # else:
        #     for i in range(l1):
        #         if nums1[i] in nums2:
        #             res.append(nums1[i])
        #             nums2.remove(nums1[i])
        # return res
        nums1.sort()                # soln2 - optimized
        nums2.sort()
        res=[]
        
        
        a=0
        b=0
        while(a<l1 and b<l2):
            if(nums1[a]==nums2[b]):
                res.append(nums1[a])
                a=a+1
                b=b+1
            elif(nums1[a]<nums2[b]):
                a=a+1
            else:
                b=b+1
        return res
