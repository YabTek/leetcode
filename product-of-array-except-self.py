class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0 for i in range(len(nums))]
        temp1 = 1
        temp2 = 1
        i = 0
        j = len(nums)-1
        while i < len(nums):
            result[i] = temp1
            temp1 *= nums[i]
            i += 1
        while j >= 0:
            result[j] *= temp2
            temp2*=nums[j]
            j-=1
        return result