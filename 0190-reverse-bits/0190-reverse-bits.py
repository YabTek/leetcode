class Solution:
    def reverseBits(self, n: int) -> int:
        ans = None
        n = bin(n)[2:]

        n = '0'*( 32-len(n) ) + n

        ans =  int( n[::-1] ,2)
        
        return ans
        