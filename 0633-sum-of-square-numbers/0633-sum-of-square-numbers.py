class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))
        
        if c == 0:
            return True

        while left < right:
            if 2*(left**2) == c:
                return True
            elif 2*(right**2) == c:
                return True
            elif (left**2) + (right**2) < c:
                left += 1
            elif (left**2) + (right**2) > c:
                right -= 1
            else:
                return True
            
        return False
                
                
            
            
        