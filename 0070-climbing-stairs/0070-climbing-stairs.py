class Solution:
    def climbStairs(self, n: int) -> int:
        self.ways = 0
        d = {}
        
        def count(n):
            if n <= 1:
                return 1
            if n not in d:
                d[n] = count(n-1) + count(n-2)
                
            return d[n]
        
        return count(n)
