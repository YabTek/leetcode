class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        best = -1
        
        while low <= high:
            mid = (low + high) // 2
            if Solution.lessthanThreshold(nums,mid,threshold):
                best = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return best
            
    def lessthanThreshold(nums,mid,threshold):
        total  = 0
        
        for num in nums:
            total += ceil(num/mid)
        
        return total <= threshold
