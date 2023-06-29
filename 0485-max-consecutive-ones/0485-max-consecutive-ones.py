class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        
        for j in range(len(nums)):
            if nums[j] == 0:
                i = j+1
            else:
                ans = max(ans,j-i+1)
                    
        return ans
        