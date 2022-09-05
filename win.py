class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        size = len(nums)-1
        return Solution.function2(0, size, nums) >= 0
        
    def function2(first, last, nums):
        if(first == last):
            return nums[first]
        scoreA = nums[first] - Solution.function2(first+1, last, nums)
        scoreB = nums[last] - Solution.function2(first, last-1, nums)
        
        return max(scoreA, scoreB)