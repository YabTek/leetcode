class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #bottom-up
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        
        return min(dp[n-1],dp[n-2])
                   
        #top-down
#         size = len(cost)
#         memo = {}
        
#         def dp(n):
#             if n >= size:
#                 return 0
#             if n == size-1:
#                 return cost[n]
#             if n not in memo:
#                 memo[n] = cost[n] + min(dp(n+1),dp(n+2))
                
#             return memo[n]
        
#         return min(dp(0),dp(1))
                
       