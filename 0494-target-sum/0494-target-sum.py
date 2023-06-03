class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def dp(idx,tot):
            
            if idx == n and tot == target:
                return 1
            elif idx >= n:
                return 0
              
            return dp(idx+1,tot+nums[idx]) + dp(idx+1,tot-nums[idx])


        return dp(0,0)
        