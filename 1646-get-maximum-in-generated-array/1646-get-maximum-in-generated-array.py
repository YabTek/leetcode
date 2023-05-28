class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        d = {}
        ans = 0
        
        def get(n):
            if n <= 1:
                return n
            if n not in d:
                if n % 2 == 0:
                    d[n] = get(n//2)
                else:
                    d[n] = get(n//2) + get(n//2 + 1)
                
            return d[n]
        
        for i in range(n,-1,-1):
            ans = max(ans,get(i))
                
        return ans
            