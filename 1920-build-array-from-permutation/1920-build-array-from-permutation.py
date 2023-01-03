class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        i = 0
        for idx in nums:
            ans[i] = nums[idx]
            i += 1
        return ans
            
        