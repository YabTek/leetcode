class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(idx,tot): 
            if idx == len(nums):
                if tot == target:
                    return 1
                return 0
            return dp(idx + 1, tot + nums[idx]) + dp(idx + 1, tot - nums[idx])      
        
        return dp(0,0)
        
        