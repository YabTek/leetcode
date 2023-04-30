class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid1)
        m = len(grid1[0])
        
        visited = set()
        ans = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def inBound(i,j):
            if 0 <= i < n and 0 <= j < m:
                return True
            
        def dfs(i,j):
            flag = grid1[i][j] == 1
            visited.add((i,j))
            
            for dr,dc in directions:
                r = dr + i
                c = dc + j
                
                if inBound(r,c) and(r,c) not in visited and grid2[r][c] == 1:
                    flag = flag & dfs(r,c)
                    
            return flag
                
        
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid2[i][j] == 1 and dfs(i,j):
                    ans += 1
                
        return ans
        
    
       