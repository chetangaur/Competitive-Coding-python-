class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        l_m=len(matrix)
        len_r=l_m
        len_c=len(matrix[0])
        
        for i in range(l_m):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    for k in range(len_c):
                        if matrix[i][k]!=0:
                            matrix[i][k]='a'
                        #print(matrix)
                    for l in range(len_r):
                        if matrix[l][j]!=0:
                            matrix[l][j]='a'
        #print(matrix)
        for i in range(l_m):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='a':
                    matrix[i][j]=0

                
        
