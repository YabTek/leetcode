class Solution:
    def countPrimes(self, n: int) -> int: 
        if n <= 1:
            return 0
        isPrime = [True] * (n)
        isPrime[0] = False
        isPrime[1] = False
        
        
#         for i in range(2,n):
#             if isPrime[i] == True:
#                 j = i * i 
#                 while j <= n:
#                     isPrime[j] = False
#                     j += i
#         return isPrime.count(True)
    
        #optimized
        
        d = 2
        while d*d < n:
            
            if isPrime[d] == True:
                j = d * d 
                while j < n:
                    isPrime[j] = False
                    j += d
            d += 1
        return isPrime.count(True)
            

        
           