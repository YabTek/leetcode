class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        def findPrime(num,primes):
            
            d = 2
            while d*d <= num:
                while num % d == 0:
                    num //= d
                    primes.add(d)
                d += 1
                
            if num > 1:
                primes.add(num)
                   
        primes = set()
        
        for i in nums:
            findPrime(i,primes)
        
        return len(primes)
        

        