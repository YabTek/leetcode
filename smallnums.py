class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        output = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    output[i] += 1
        return output
        
        