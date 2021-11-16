class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l=len(nums)                     # method 1 --> O(n2)
        # res=[]
        # for i in range(0,l):
        #     for j in range(i+1,l):
        #         if nums[i]+nums[j]==target:
        #             res.append(i)
        #             res.append(j)
        # return res
        l=len(nums)
        res={}                        # method 2 --> O(n) using dict/hashing
        ans=[]
        for i in range(l):
            if target-nums[i] in res.keys():
                ans.append(res[target-nums[i]])
                ans.append(i)
                return ans
            else:
                res[nums[i]]=i
            
                    
        
        
