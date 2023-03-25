class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        nums.append(-1)
        
        i = 0
        while i < len(nums):
            if nums[i] == i or nums[i] == -1:
                i += 1
                
            else:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                if nums[i] == -1 or nums[nums[i]] == -1:
                    ans = i
              
        return ans