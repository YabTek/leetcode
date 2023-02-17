class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    temp.append([i,j])
        
        for k in range(len(temp)):
            for i in range(row):
                matrix[i][temp[k][1]] = 0
            for j in range(col):
                matrix[temp[k][0]][j] = 0

        
                
        