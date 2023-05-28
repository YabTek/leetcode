class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ans = 0
        prefix = 0
        store = 0
        
        satisfaction.sort()
        for i in range(len(satisfaction)-1,-1,-1):
            prefix += satisfaction[i]
            store += prefix
            ans = max(ans, store)
        
        return ans
                
        