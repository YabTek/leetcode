class Solution:
    def countBits(self, n: int) -> List[int]:
        def binary(n,rep):
            while n > 0:
                if (n & 1) == 1:
                    rep += 1
                n = n >> 1
            return rep
            
        ans = [0] * (n + 1) 
       
        for num in range(n+1):
            ans[num] = binary(num,0)
        return ans
        
        