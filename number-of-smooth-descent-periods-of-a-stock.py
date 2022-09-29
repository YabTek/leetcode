class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        size = len(prices)
        counter = [1] * size
        for day in range(size-1):
            if prices[day] == prices[day+1]+1:
                counter[day+1] = counter[day]+1
        return sum(counter)
       