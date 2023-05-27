class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        ans = float("-inf")
        
        for i in range(len(nums)):
            total += nums[i]
            len_ = i+1
            ans = max(ans,math.ceil(total/len_))
            
        return ans
            
        
        