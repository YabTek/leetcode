class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        n = len(timeSeries)
        
        for i in range(n - 1):
            ans += min(duration, timeSeries[i+1] - timeSeries[i])
        
        return ans + duration