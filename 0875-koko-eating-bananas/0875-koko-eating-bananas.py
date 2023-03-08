class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 
        high = max(piles)
    
        while low <= high:
            mid = (high + low) // 2
            
            if Solution.isLessthanH(piles,h,mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
            
    def isLessthanH(piles,h,mid):
        total = 0
        
        for num in piles:
            total += ceil(num/mid)
            
        return   total <= h
       


    
        