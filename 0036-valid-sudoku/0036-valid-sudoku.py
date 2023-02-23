class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = defaultdict(set)
        col = defaultdict(set)
        row = defaultdict(set)
        board_size = 9
        
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in grid[(i//3,j//3)]):
                    return False
                grid[(i//3,j//3)].add(board[i][j])
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                           
        return True
        