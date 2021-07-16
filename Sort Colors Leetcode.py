class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ini_index=0
        for i in range(0,3):
            length=len(nums)
            for j in range(0,length):
                if(nums[j]==i):
                    nums[j],nums[ini_index]=nums[ini_index],nums[j]
                    ini_index=ini_index+1
        return nums
                
                
        
        
