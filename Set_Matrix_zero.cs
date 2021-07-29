public class Solution {
    public void SetZeroes(int[][] matrix) {
        int l_m=matrix.Length;
        int len_r=l_m;
        int len_c = matrix[0].Length;
        for(int i=0;i<l_m;i++)
        {
            for(int j=0;j<matrix[i].Length;j++)
            {
                if(matrix[i][j]==0)
                {
                    for(int k=0;k<len_c;k++)
                    {
                        if(matrix[i][k]!=0)
                        {
                            matrix[i][k]='a';
                            
                        }
                        
                    }
                    for(int l=0;l<len_r;l++)
                    {
                        if(matrix[l][j]!=0)
                        {
                            matrix[l][j]='a';
                        }
                    }
                    
                }
                
            }
            
        }
        for(int i=0;i<l_m;i++)
        {
            for(int j=0;j<matrix[i].Length;j++)
            {
                if(matrix[i][j]=='a')
                {
                    matrix[i][j]=0;
                }
            }
        }
        
        
    }
}
