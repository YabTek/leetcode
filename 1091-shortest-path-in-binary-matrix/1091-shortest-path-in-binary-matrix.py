class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque([(0,0,1)])
        size = len(grid)
        
        if grid[0][0] == 1:
            return -1
       
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)] 
        
        def isInBound(row,col):
            if 0 <= row < size and 0 <= col < size:
                return True
        
        while queue:
            row,col,len_ = queue.popleft()
            
            if row == col == size-1:
                return len_
            
            for a,b in directions:
                new_row = row + a
                new_col = col + b
                
                if isInBound(new_row,new_col) and grid[new_row][new_col] == 0 and (new_row,new_col) not in visited:
                    visited.add((new_row,new_col))
                    queue.append((new_row,new_col,len_ + 1))
            
        return -1
       