class Solution:
    def rob(self, nums: List[int]) -> int:
        d = {}       
        
        def dp(i):
            if i < 0:
                return 0
            if i == 1:
                return max(nums[0],nums[1])
            if i not in d:
                d[i] = max((nums[i]+dp(i-2)),dp(i-1))
                
            return d[i]
        
        return dp(len(nums)-1)
        