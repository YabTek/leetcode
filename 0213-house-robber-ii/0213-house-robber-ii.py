class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dict_right = {}
        def dp1(i):
            if i <= 0:
                return 0
            if i not in dict_right:
                dict_right[i] = max(nums[i]+dp1(i-2),dp1(i-1))
            
            return dict_right[i]
        
        dict_left = {}
        def dp2(i):
            if i >= n-1:
                return 0
            if i not in dict_left:
                dict_left[i] = max(nums[i]+dp2(i+2),dp2(i+1))
                
            return dict_left[i]
            
        
        return max(dp1(n-1),dp2(0))
        