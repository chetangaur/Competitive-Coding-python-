class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res_arr=[]
        if(numRows==1):
            res_arr=[[1]]
            return res_arr
        elif(numRows==2):
            res_arr=[[1],[1,1]]
            return res_arr
        else:
    
            
            for i in range(1,numRows+1):
                arr=[0]*i
                res_arr.append(arr)
            #ra_l=len(res_arr)
            res_arr[0]=[1]
            res_arr[1]=[1,1]
            count=1
            for i in range(2,numRows):
                for j in range(1,len(res_arr[i])-1):
                    res_arr[i][0]=res_arr[i-1][0]
                    res_arr[i][j]=res_arr[i-1][j-1]+res_arr[i-1][j]
                    res_arr[i][-1]=res_arr[i-1][-1]
            return res_arr



        
