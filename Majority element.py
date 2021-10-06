class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''res=[]                            # method 1
        len_nums=len(nums)
        set_A=set(nums)
        for ele in set_A:
            if(nums.count(ele)>len_nums/2):
                return ele'''
        dict_A={}                           # method 2
        l=len(nums)
        for i in range(l):
            if nums[i] not in dict_A:
                dict_A[nums[i]]=1
                #dict_A.update(nums[i]:1)
                if dict_A[nums[i]]>l/2:
                    return nums[i]
            else:
                dict_A[nums[i]]=dict_A[nums[i]]+1
                if dict_A[nums[i]]>l/2:
                    return nums[i]
        '''l=len(nums)                 # method 3
        count=0
        majority_ele=nums[0]
        for i in range(l):
            if nums[i]==majority_ele:
                count=count+1
            else:
                count=count-1
            if count<=0:
                majority_ele=nums[i]
        return majority_ele'''                # Moore voting algo not imlemented correctly
                
            
            
        
                
        
        
        
