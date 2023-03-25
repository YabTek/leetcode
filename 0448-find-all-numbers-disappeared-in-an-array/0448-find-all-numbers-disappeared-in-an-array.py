class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            if  i == nums[i]-1 or  nums[nums[i]-1] == nums[i]:
                i += 1
            else:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
                
        for i in range(len(nums)):
            if i != nums[i] - 1:
                ans.append(i+1)
            
        return ans
            
        