class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = [inf] * len(prices)
        dp = [0]*len(prices)
        
        buy[0] = prices[0]
        dp[0] = 0
        
        for i in range(1,len(prices)):
            buy[i] = min(buy[i-1],prices[i]-dp[i-1])
            dp[i] = max(dp[i-1],prices[i]-buy[i-1]-fee)
            
        return dp[-1]
        