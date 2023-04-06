class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def find_gcd(a,b):
            if b == 0:
                return a
            else:
                return find_gcd(b,a%b)
            
        gcd = 0 
        ans = 0
        n = len(nums)
        
        for i in range(n):
            gcd = nums[i]
            for j in range(i,n):
                gcd = find_gcd(gcd, nums[j])   
                if gcd == k:
                    ans += 1

        return ans

            
