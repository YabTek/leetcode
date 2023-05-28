class Solution:
    def tribonacci(self, n: int) -> int:
        d = {}
        def tribo(n):
            if  n <= 1:
                d[n] = n
            if n == 2:
                d[n] = 1
            if n not in d:
                d[n] = tribo(n-1) + tribo(n-2) + tribo(n-3)
            return d[n]
        
        return tribo(n)
        