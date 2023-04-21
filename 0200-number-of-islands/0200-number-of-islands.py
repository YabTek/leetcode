class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n= len(grid)
        m = len(grid[0])
        
        def isBound(i,j):
            if i >= 0 and i < n and j >= 0 and j < m:
                return True

        def dfs(i, j):
            if isBound(i,j) and grid[i][j] == '1':

                grid[i][j] = 'visited'
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans+=1       

        return ans

                    
        