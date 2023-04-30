class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
    
        def inBound(i,j):
            if 0 <= i < n and 0 <= j < m:
                return True
            
        def dfs(row,col):
            
            if not inBound(row,col) or grid[row][col] == 0:
                return 1
            if (row,col) in visited:
                return 0
            
            total = 0
            visited.add((row,col))
            
            for r,c in directions:
                new_row = r + row
                new_col = c + col
                
                total += dfs(new_row,new_col)
                    
            return total
           
        
        
        n = len(grid)
        m = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i,j)
                    
                    
    
        
            
        