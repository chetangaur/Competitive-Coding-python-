# time comp O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=100000
        max_profit=0
        l=len(prices)
        for i in range(l):
            if prices[i]<minprice:
                minprice=prices[i]
            elif(prices[i]-minprice>max_profit):
                max_profit=prices[i]-minprice
        return max_profit

      
# time com O(n2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_p=len(prices)
        nl=[]
        res=[]
        if l_p==1:
            return 0
        else:
            for i in range(l_p-1):
                nl=prices[i+1:]
                res.append(max(nl)-prices[i])
            ans=max(res)
            if ans>0:
                return ans
            else:
                return 0
