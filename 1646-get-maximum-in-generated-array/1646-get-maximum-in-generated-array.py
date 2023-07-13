class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {}
        ans = 0
        
        def dp(n):
            if n <= 1:
                memo[n] = n
                return n
            if n not in memo:
                if n % 2 == 0:
                    memo[n] = dp(n//2)
                else:
                    memo[n] = dp(n//2) + dp(n//2+1)
                    
            return memo[n]
            
        dp(n)
        for i in range(n):
            if i not in memo:
                dp(i)
                
        return max(memo.values())
    
            
       