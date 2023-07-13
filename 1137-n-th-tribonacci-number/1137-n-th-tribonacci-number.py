class Solution:
    def tribonacci(self, n: int) -> int:
        #bottom up
        if n <= 1:
            return n
        
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            
        return dp[n]
    
    #top down
#         memo = {}
#         def dp(n):
#             if n <= 1:
#                 return n
#             if n == 2:
#                 return 1
#             if n not in memo:
#                 memo[n] = dp(n-1)+dp(n-2)+dp(n-3)
#             return memo[n]
            
        
#         return dp(n)

      