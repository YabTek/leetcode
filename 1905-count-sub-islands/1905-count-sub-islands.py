class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    
        n = len(grid2)
        m = len(grid2[0])
        
        def inBound(i,j):
            if 0 <= i < n and 0 <= j < m:
                return True
        def dfs(i, j):
            temp = grid1[i][j] == 1
            visited.add((i,j))

            for a, b in directions:
                new_row = a + i
                new_col = b + j
                
                if inBound(new_row,new_col) and grid2[new_row][new_col] == 1 and (new_row,new_col) not in visited:
                    temp = dfs(new_row,new_col) and temp
            return temp
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()
        ans = 0

        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid2[i][j] == 1:
                    if dfs(i,j):
                        ans += 1
        return ans
        