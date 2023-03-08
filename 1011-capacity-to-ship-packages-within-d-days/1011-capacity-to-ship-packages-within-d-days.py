class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def countDays(mid):
            total = 0
            days = 1

            for weight in weights:
                if total > mid - weight:
                    total = weight
                    days += 1
                else:
                    total += weight
           
            return days
 
        prefix_sum = list(accumulate(weights))    
        left = max(weights)
        right = sum(weights)
        
        while left <= right:
            mid = left + (right - left)//2
            if countDays(mid) > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
