class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(sqrt(c))

        while i <= j:
            tot = i**2 + j**2
            if tot < c:
                i += 1
            elif tot > c:
                j -= 1
            else:
                return True

        return False
        
        

        