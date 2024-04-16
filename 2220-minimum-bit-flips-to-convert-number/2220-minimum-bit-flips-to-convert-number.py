class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal  
        ans = 0
        
        while xor:
            xor &= xor - 1  
            ans += 1

        return ans