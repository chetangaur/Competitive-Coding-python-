class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a=intervals[0]
        res=[]
        count=0
        l=len(intervals)
        for i in range(l):
            if(a[1]>=intervals[i][0]):
                a=[a[0],max(intervals[i][1],a[1])]
            else:
                count=count+1
                res.append(a)
                a=intervals[i]
        if count!=0:
            a=[a[0],max(intervals[-1][1],a[1])]
            res.append(a)
            return res
        else:
            return [a]
            

                
        
        
        
