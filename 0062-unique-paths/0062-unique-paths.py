class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
 
        
        #bottom-up
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if row >= m-1 or col >= n-1:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row+1][col] + dp[row][col+1]
                        
        return dp[0][0]
       
