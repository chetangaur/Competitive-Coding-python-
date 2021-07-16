public class Solution {
    public void SortColors(int[] nums) {
        int ini_index=0;
        int temp_var=0;
        for(int i=0;i<3;i++)
        {
            int length=nums.Length;
            for(int j=0;j<length;j++)
            {
                if(nums[j]==i)
                {
                    temp_var=nums[j];
                    nums[j]=nums[ini_index];
                    nums[ini_index]=temp_var;
                    ini_index++;


                }
                
            }
            
        }
        
        
        
    }
}
