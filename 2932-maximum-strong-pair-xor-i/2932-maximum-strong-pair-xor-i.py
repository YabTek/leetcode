class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i, n):
                num1 = nums[i]
                num2 = nums[j]
                if abs(num1 - num2) <= min(num1, num2):
                    ans = max(ans, num1 ^ num2)
                    
        return ans
                
        