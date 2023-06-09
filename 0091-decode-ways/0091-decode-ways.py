class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def dp(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            
            count = 0
            if s[i-1] != "0":
                count += dp(i-1)
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                count += dp(i-2)
                
            return count
        
        return dp(len(s))