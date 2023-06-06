class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        for num in nums:
            maxOr |= num
        ans = 0

        def backtrack(i, curOr):
            nonlocal maxOr, ans

            if i == len(nums) and curOr == maxOr:
                return 1
            elif i >= len(nums):
                return 0
            return backtrack(i + 1, curOr | nums[i]) + backtrack(i + 1, curOr)

        return backtrack(0, 0)

        
        