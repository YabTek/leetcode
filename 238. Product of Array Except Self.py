class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = 1

        prod = 1
        for i in range(n):
            ans[i] = prod
            prod *= nums[i]

        prod = 1
        for i in range(n-1, -1, -1):
            ans[i] *= prod
            prod *= nums[i] 

        return ans

        