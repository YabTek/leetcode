class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        ans = 0
        num_of_fresh = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    num_of_fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
                    
        def inBound(i,j):
            if 0 <= i < n and 0 <= j < m:
                return True
                    
        while queue and num_of_fresh > 0:
            for i in range(len(queue)):
                row,col = queue.popleft()
                
                for a,b in direction:
                    new_row = a + row
                    new_col = b + col
                    
                    if inBound(new_row,new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        num_of_fresh -= 1
                        queue.append((new_row,new_col))
              
            ans += 1
                
        if num_of_fresh == 0:
            return ans
        else:
            return -1
                    
        