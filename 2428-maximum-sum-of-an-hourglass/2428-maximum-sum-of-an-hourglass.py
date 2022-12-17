class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        ans = -float("inf")
        row = len(grid)-1
        col = len(grid[0])-1
        
        for i in range(row-1):
            for j in range(col-1):
                center = Solution.center(grid,i,j)
                top = Solution.topSum(grid,i,j)
                bottom = Solution.bottomSum(grid,i,j)
                
                pre_sum =  center + top + bottom
                ans = max(ans,pre_sum)
        return ans 

    def topSum(grid,i,j):
            return grid[i][j] + grid[i][j+1] + grid[i][j+2]
        
    def bottomSum(grid,i,j):
            return grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
        
    def center(grid,i,j):
            return grid[i+1][j+1]
       
				
        