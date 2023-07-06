class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        group_i = []
        group_j = []
        n = len(values)
        
        for i in range(n):
            group_i.append(values[i]+i)
            group_j.append(values[i]-i)
            
        for i in range(n-2,-1,-1):
            group_j[i] = max(group_j[i],group_j[i+1])
        
        ans = -inf
        for i in range(n-1):
            ans = max(ans,group_i[i]+group_j[i+1])
            
        return ans
            
        