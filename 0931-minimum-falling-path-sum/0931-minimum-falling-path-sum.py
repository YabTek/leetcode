class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = matrix
        directions = [(1,0),(1,1),(1,-1)]
        
        def isInBound(row,col):
            return 0 <= row < n and 0 <= col < m
        
        for row in range(n-2,-1,-1):
            for col in range(m-1,-1,-1):
                min_ = inf
                for r,c in directions:
                    new_r = row + r
                    new_c = col + c
                    
                    if isInBound(new_r,new_c):
                        min_ = min(min_,dp[new_r][new_c])
                        
                dp[row][col] += min_
                        
        return min(dp[0])
                    
                
                
        