class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True]*(right+1)
        isPrime[0] = False
        isPrime[1] = False
        
        i = 2
        
        while i*i <= right:
            if isPrime[i]:
                j = i*i
                while j <= right:
                    isPrime[j] = False
                    j += i
            i += 1
            
        primes = []
        min_ = float("inf")
        ans = [-1,-1]
        
        for i in range(left,right+1):
            if isPrime[i] == True:
                primes.append(i)
                
        for i in range(1,len(primes)):
            diff = primes[i]-primes[i-1]
            nums = [primes[i-1],primes[i]]

            if  diff < min_:
                ans = nums
                min_ = diff
            if diff == min_ and nums[0]<ans[0]:
                ans = nums

                
                
        return ans
        
                
                
        