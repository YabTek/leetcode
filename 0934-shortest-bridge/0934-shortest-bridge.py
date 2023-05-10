class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        n = len(grid)
        self.ans = 0
        
        def IsInBound(i, j):
            if 0 <= i < n and 0 <= j < n:
                return True        
        
        def dfs(i, j):
            visited.add((i,j))
            
            for a,b in directions:
                x = a + i
                y = b + j
                if IsInBound(x,y) and (x,y) not in visited and grid[x][y]:
                    dfs(x,y)

           
        def checkOneIsland():  
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        dfs(i,j)
                        return
                    
        
        def bfs(queue):
                
            while queue:

                for i in range(len(queue)):
                    r, c = queue.popleft()

                    for a,b in directions:
                        x = r + a
                        y = c + b

                        if IsInBound(x, y) and (x, y) not in visited:
                            if grid[x][y] == 1:
                                return self.ans
                            visited.add((x,y))
                            queue.append((x, y))

                self.ans += 1
                
                
        checkOneIsland()
        
        return bfs(deque(visited))
