class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        
        xor = bin(x^y)
        for bit in str(xor):
            if bit == '1':
                ans += 1
                
        return ans
        