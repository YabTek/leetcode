class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        stk = []
        n = len(nums)
        
        for i in range(2*n):
            i %= n
            while stk and nums[i] > nums[stk[-1]]:
                ans[stk.pop()] = nums[i]
            stk.append(i)
                    
        return ans
        
        