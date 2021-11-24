# class Solution:
#     def sortColors(self, nums: List[int]) -> None:        # method 1 --> t=O(n2)
#         ini_index=0
#         for i in range(0,3):
#             length=len(nums)                                        
#             for j in range(0,length):
#                 if(nums[j]==i):
#                     nums[j],nums[ini_index]=nums[ini_index],nums[j]
#                     ini_index=ini_index+1
#         return nums
                
class Solution:
    def sortColors(self, nums: List[int]) -> None:             # method 2 -- O(n)  [ single traversal]
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        low=0
        mid=0
        high=l-1
        while(mid<=high):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low=low+1
                mid=mid+1
            elif(nums[mid]==1):
                mid=mid+1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high=high-1
                
        return nums
    
    
    
    # another method will be traverse through array and count number of 0,1,2 and place them indexvise     [ 2 traversal]
                
        
        
