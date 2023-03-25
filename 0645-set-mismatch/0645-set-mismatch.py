class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        ans = []
        
        while i < n:
            if i == nums[i] - 1 or nums[i] == nums[nums[i]-1]:
                i += 1
            else:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
                
        for i in range(n):
            if i != nums[i] - 1:
                ans.append(nums[i])
                ans.append(i + 1)
            
        return ans