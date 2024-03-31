class Solution:
    def hammingWeight(self, n: int) -> int:
        self.ans = 0
        
        def count(n):
            while n:
                if (n & 1):
                    self.ans += 1
                n >>= 1
            return self.ans
        
        return count(n)