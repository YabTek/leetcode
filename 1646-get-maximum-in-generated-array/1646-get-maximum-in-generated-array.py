class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        #bottom-up
        if n == 0:
            return 0
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2,n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + dp[i//2 + 1]
                
        return max(dp)
        
          #top-down
#         memo = {}
#         ans = 0
        
#         def dp(n):
#             if n <= 1:
#                 return n
#             if n not in memo:
#                 if n % 2 == 0:
#                     memo[n] = dp(n//2)
#                 else:
#                     memo[n] = dp(n//2) + dp(n//2+1)
                    
#             return memo[n]
            
       
#         for i in range(n+1):
#             ans = max(ans,dp(i))
                
#         return ans
            
       