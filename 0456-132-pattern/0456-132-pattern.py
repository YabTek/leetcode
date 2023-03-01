class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stk = []
        min_ = nums[0]

        for i in range(1,len(nums)):
            while stk and nums[i] >= stk[-1][1]:
                stk.pop()
            if stk and stk[-1][0] < nums[i] < stk[-1][1]:
                return True
            stk.append([min_,nums[i]])
            min_ = min(min_, nums[i])
            
        return False
            
        