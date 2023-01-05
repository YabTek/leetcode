class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countX = 0
        countO = 0
        X_wins = False
        O_wins = False
        
        #number of X and O 
        for row in board:
            countX += row.count('X')
            countO += row.count('O')
            
        #checking row for the winner
        for row in board:
            if row == "XXX":
                X_wins = True
                break
            elif row == "OOO":
                O_wins = True
                break
                
        #checking column for the winner
        for col in zip(*board):
            if col == ('X','X','X'):
                X_wins = True
                break
            if col == ('O','O','O'):
                O_wins = True
                break
                
        #checking diagonal for the winner
        for diagonal in board:
            if board[0][0] == board[1][1] == board[2][2] == 'X':
                X_wins = True
                break
            if board[0][0] == board[1][1] == board[2][2] == 'O':
                O_wins = True
                break
            if board[0][2] == board[1][1] == board[2][0] == 'X':
                X_wins = True
                break
            if board[0][2] == board[1][1] == board[2][0] == 'O':
                O_wins = True
                break
       
        if X_wins == False and O_wins == False:
            return (countX == countO + 1) or (countX == countO)
        elif X_wins:
            return  countX == countO + 1
        elif O_wins:
            return countO == countX
            
            
        
        
       
            
        