class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        queue = deque()
        
        def isInBound(i,j):
            if 0 <= i < n and 0 <= j < m:
                return True
        
        def bfs(queue):
            
            while queue:
                r,c,len_ = queue.popleft()
                for a,b in directions:
                    row = r + a
                    col = c + b
                     
                    if isInBound(row,col) and (row,col) not in visited and mat[row][col] == 1:
                        ans[row][col] = len_ + 1
                        visited.add((row,col))
                        queue.append((row,col,len_ + 1))
 
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append([i,j,0])

        bfs(queue)       
        return ans
                    
                
                
        