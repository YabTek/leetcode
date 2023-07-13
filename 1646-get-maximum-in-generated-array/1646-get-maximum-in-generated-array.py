class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {}
        ans = 0
        
        def dp(n):
            if n <= 1:
                return n
            if n not in memo:
                if n % 2 == 0:
                    memo[n] = dp(n//2)
                else:
                    memo[n] = dp(n//2) + dp(n//2+1)
                    
            return memo[n]
            
       
        for i in range(n+1):
            ans = max(ans,dp(i))
                
        return ans
            
       