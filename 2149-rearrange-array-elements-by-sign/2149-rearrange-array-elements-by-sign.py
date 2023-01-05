class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        i = 0
        for num in nums:
            if num > 0 and i < len(nums):
                ans[i] = num
                i+=2
        j = 1
        for num in nums:
            if num < 0 and j<len(nums):
                ans[j] = num
                j+=2
        
        return ans
        