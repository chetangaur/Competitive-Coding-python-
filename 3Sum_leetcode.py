nums=[-1,0,1,2,-1,-4]                        # method 1 
res=[]
store_dict={}
l=len(nums)
nums.sort()
for ele in nums:
    if ele not in store_dict:
        store_dict[ele]=1
    else:
        store_dict[ele]=store_dict[ele]+1
print(store_dict)
for i in range(l):
    t2=store_dict[nums[i]]                                 # need to modify some code here
    store_dict.pop(nums[i])        

    for j in range(i+1,l):
        t1=store_dict[nums[j]]
        store_dict.pop(nums[j])
        k=nums[i]+nums[j]
        if -k in store_dict:
            res.append([nums[i],nums[j],-k])
        store_dict[nums[j]]=t1
    store_dict[nums[i]]=t2
        
print(res)
for ele in res:
    ele.sort()
print(res)
ans=[]
for ele in res:
    if ele not in ans:
        ans.append(ele)
print(ans)        
  
  
  
  
  
  
  
  nums.sort()                                                    # method 2 --> optimized --> work for all 2,3,4 Sum                     
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            s,e = i+1, N-1
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result
