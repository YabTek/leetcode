class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        
        def isMagicSquare(x,y,z):
            unique = set(x+y+z)
            random_unique = set(range(1,10))
          
            sum1 = sum(x) == sum(y) == sum(z) == x[0]+y[0]+z[0]
            sum2 = x[1]+y[1]+z[1] == x[2]+y[2]+z[2] == x[0]+y[1]+z[2] == x[2]+y[1]+z[0]
            
            return ((unique == random_unique) and (sum1 and sum2))
        
        for r in range(row - 2):
            for c in range(col - 2): 
                lst1 = [grid[r][c],grid[r][c+1],grid[r][c+2]]
                lst2 = [grid[r+1][c],grid[r+1][c+1],grid[r+1][c+2]]
                lst3 = [grid[r+2][c],grid[r+2][c+1],grid[r+2][c+2]]
             
                if isMagicSquare(lst1,lst2,lst3):
                    count += 1
                    
        return count
