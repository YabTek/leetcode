class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def dp(i,cur):
            if i >= n:
                return 0
            
            if cur == "buy":
                return max(dp(i+1,"sell") - prices[i], dp(i+1,"buy"))
            
            if cur == "sell":
                return max(dp(i+1,"cooldown") + prices[i], dp(i+1,"sell"))
            
            if cur == "cooldown":
                return dp(i+1,"buy")
            
        return dp(0,"buy")
            
       
        
        