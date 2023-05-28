class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = {}
        size = len(cost)
        
        def dp(n):
            if n >= size:
                return 0
            if n == size-1:
                return cost[n]
            if n not in d:
                d[n] = cost[n] + min(dp(n+1),dp(n+2))
            return d[n]
        
        return min(dp(0), dp(1))

        