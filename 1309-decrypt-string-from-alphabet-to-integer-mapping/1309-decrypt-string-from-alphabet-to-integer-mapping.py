class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = 0
        n = len(s)-1
        
        while i <= n:
            if i + 2 < len(s) and s[i+2] == '#':
                string = s[i:i+2]
                i += 2
            elif s[i] != '#':
                string = s[i]   
            ans += chr(int(string)+96)
            i += 1
            
        return ans
       

            
           