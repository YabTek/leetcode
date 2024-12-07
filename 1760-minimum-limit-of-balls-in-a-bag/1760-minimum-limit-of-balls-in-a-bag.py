class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)
        
        def countOperations(num):
            operations = 0
            for balls in nums:
                operations += (balls - 1) // num
            return operations
        
        while left < right:
            mid = (left + right) // 2
            if countOperations(mid) <= maxOperations:
                right = mid
            else:
                left = mid + 1
                
        return left
        