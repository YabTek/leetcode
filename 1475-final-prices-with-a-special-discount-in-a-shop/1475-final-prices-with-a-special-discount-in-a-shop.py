class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = prices
        stk = []
        
        for i in range(n):
            nxt = prices[i]
            while stk and  nxt <= prices[stk[-1]]:
                idx = stk.pop()
                ans[idx] = prices[idx] - nxt
            stk.append(i)
            
        return ans