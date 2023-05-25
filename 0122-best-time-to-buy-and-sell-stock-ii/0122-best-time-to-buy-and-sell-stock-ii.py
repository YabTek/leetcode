class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        
        for i in range(len(prices)-1):
            cur = prices[i]
            nxt = prices[i+1]
            if cur < nxt:
                total += nxt-cur

        return total
                