class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        end = 2**p-1 
        modulo =10**9+7
        return (pow(2*p-2, 2(p-1) - 1, modulo) * (end)) % (modulo)