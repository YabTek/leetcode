class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_perimeter = -float("inf")
        
        for i in range(len(nums)-2):
            sliced = nums[i:i+3]
            
            if sliced[0] + sliced[1] > sliced[2]:
                tot = sum(sliced)
                max_perimeter = max(max_perimeter,tot)
                
        if max_perimeter == -inf:
            return 0
        return max_perimeter
         