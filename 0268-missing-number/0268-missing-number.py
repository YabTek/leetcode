class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        
        i = 0
        while i < len(nums):
            if nums[i] == i or nums[i] == -1:
                i += 1
                
            else:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        return nums.index(-1)
              
