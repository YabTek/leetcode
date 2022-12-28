class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        next = 1
        if n % 2 == 0:
            return n
        else:
            next += 1
            n *= next
            return Solution.smallestEvenMultiple(self,n)
       