  def containsDuplicate(self, nums: List[int]) -> bool:
        # res=list(set(nums))             # soln 1
        # if len(nums)==len(res):
        #     return False
        # else:
        #     return True
        
    
        
        nums.sort()                     # soln 2
        for i in range(l-1):
            if nums[i]==nums[i+1]:
                return True
        return False
