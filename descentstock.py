class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result,counter = 0 ,0
        size = len(prices)
        days = 0
        while days < len(prices):
            if prices[days-1] == prices[days]+1:
                counter += 1
            else: 
                counter = 1
            result += counter
            days += 1
        return result