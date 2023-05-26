class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        ans = float("inf")
        temp = nums.copy()
        
        for i in range(3):
            nums[i] = nums[3]
        ans = min(ans,nums[-1]-nums[0])
        nums = temp
        temp = nums.copy()
        
        for i in range(n-1,n-4,-1):
            nums[i] = nums[-4]
        ans = min(ans,nums[-1]-nums[0])
        nums = temp
        temp = nums.copy()
        
        nums[0] = nums[1] = nums[2]
        nums[-1] = nums[-2] 
        ans = min(ans,nums[-1]-nums[0])
        nums = temp
        temp = nums.copy()

        
        nums[-1] = nums[-2] = nums[-3]
        nums[0] = nums[1]
        ans = min(ans,nums[-1]-nums[0])
        nums = temp
        temp = nums.copy()

        
        return ans
            
        
        