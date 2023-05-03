class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def isBoundary(i,j):
            if (board[i][j] == 'O') and (i in [0,row-1] or j in [0,col-1]):
                return True
            
        def isInBound(i,j):
            if 0 <= i < row and 0 <= j < col:
                return True
        
        def dfs(i,j):
            
            for a,b in directions:
                new_row = i + a
                new_col = j + b
            
                if isInBound(new_row,new_col) and board[new_row][new_col]=='O':
                    board[new_row][new_col]="unsurrounded"
                    dfs(new_row,new_col)
       
        for i in range(row):
            for j in range(col):
                if isBoundary(i,j):
                    board[i][j]='unsurrounded'
                    dfs(i,j)
                    
        for i in range(row):
            for j in range(col):
                if board[i][j]=='unsurrounded':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
       