class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = []
        ans = []
        
        if r*c != len(mat)*len(mat[0]):
            return mat

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                temp.append(mat[row][col])
                
        for row in range(0,len(temp),c):
            ans.append(temp[row : row+c])
            
        return ans
        