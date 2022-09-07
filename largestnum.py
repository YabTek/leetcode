import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        idx = 0
        while idx < len(nums):
            nums[idx] = str(nums[idx])
            idx+=1
            
        def greater(num1,num2):
            if num1+num2 <= num2 +num1:
                return 1
            else:
                return -1
        nums = sorted(nums, key = functools.cmp_to_key(greater))
        temp =int("".join(nums))
        result = str(temp)
        
        return result