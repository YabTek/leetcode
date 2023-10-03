class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
       
        @cache
        def dp(i, j):
          
            if i >= n or j < 0:
                return 0
            if s[i] == s[j]:
                return dp(i + 1, j - 1) + 1
            else:
                return max(dp(i + 1, j), dp(i, j - 1))
        
        return dp(0, n - 1)





