def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)                          # soln 1
        # k=k%n
        # nums[:]=nums[n-k:]+nums[:n-k]
    
        
        def rev(arr: List[int],start: int,end: int) -> None:    # soln 2
            while(start<end):
                arr[start],arr[end]=arr[end],arr[start]
                start=start+1
                end=end-1
                 
        l=len(nums)
        k=k%l
        if (l<=1):
            return
        else:
            
            rev(nums,0,l-1)
            rev(nums,0,k-1)
            rev(nums,k,l-1)
            
   #         while(k>0):-
#             temp=nums[-1]                                  # brute force but have tle
#             l=len(nums)
        
#             for i in range(l-2,-1,-1):
#                 nums[i+1]=nums[i]
#             nums[0]=temp
#             k=k-1
