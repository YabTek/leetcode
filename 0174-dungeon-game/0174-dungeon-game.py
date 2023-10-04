class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        
        dp = [[inf for i in range(m+1)] for j in range(n+1)] 
        
        dp[n][m-1] = 1
        dp[n-1][m] = 1
        

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                diff = min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j]
                if diff < 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = diff
                    
        return dp[0][0]
                    
                   
                                 