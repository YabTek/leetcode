class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target + 1)
        
        for i in range (1, target + 1):
            for j in range(len(nums)):
                if i > nums[j]:
                    dp[i] += dp[i - nums[j]]
                if i == nums[j]:
                    dp[i] += 1
                
        
        return dp[target]
        