class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        ans = -float("inf")
        row = len(grid)-1
        col = len(grid[0])-1
        
        for i in range(row-1):
            for j in range(col-1):
                center = grid[i+1][j+1]
                top_sum =  grid[i][j] + grid[i][j+1] + grid[i][j+2]
                bottom_sum = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                
                pre_sum =  center + top_sum + bottom_sum
                ans = max(ans,pre_sum)
                
        return ans 

    
       
				
        