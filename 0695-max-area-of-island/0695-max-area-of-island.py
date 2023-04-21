class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        ans = 0
        
        def inBound(i,j):
            if i >= 0 and i < n and j >= 0 and j < m:
                return True
            
        def dfs(i,j): 
            if not inBound(i,j) or grid[i][j] != 1:
                return 0
            if inBound(i,j) and grid[i][j] == 1:
                grid[i][j] = "visited"
                return 1 + dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    temp = 0
                    ans = max(ans,dfs(i,j))
                    
        return ans


        