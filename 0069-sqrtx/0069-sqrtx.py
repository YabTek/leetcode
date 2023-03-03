class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        best = -1
        while left <= right:
            mid = left + (right - left) // 2
            
            if mid ** 2 <= x:
                best = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return best