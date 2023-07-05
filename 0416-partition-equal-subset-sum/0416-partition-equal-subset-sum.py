class Solution:
    def canPartition(self, nums: List[int]) -> bool:    
        total = sum(nums)
    
        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}  

        def dp(i, target):
            if target == 0:
                return True
            if i == 0 or target < 0:
                return False

            if (i, target) in memo:
                return memo[(i, target)]

            memo[(i, target)] = dp(i-1, target - nums[i - 1]) or dp(i - 1, target)

            
            return memo[(i, target)] 

        return dp(len(nums), target)
