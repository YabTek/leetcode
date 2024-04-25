class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        max_ = 0
        n = len(s)
        
        for i in range(n):
            l = i
            r = i + 1
            
            while l >= 0 and r < n and s[l] == s[r]:
                len_ = r - l + 1
                if len_ > max_:
                    ans = s[l:r+1]
                    max_ = len_
                l -= 1
                r += 1
                
            l = i
            r = i 
            
            while l >= 0 and r < n and s[l] == s[r]:
                len_ = r - l + 1
                if len_ > max_:
                    ans = s[l:r+1]
                    max_ = len_
                l -= 1
                r += 1
                
        return ans
            
            
        