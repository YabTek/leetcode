class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                return 0
            if (i,j) not in d:
                d[(i,j)] = dp(i+1,j) + dp(i,j+1)
                
            return d[(i,j)]
        
        d = {}
        return dp(0,0)   
        
