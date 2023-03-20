class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        i = 0
        
        def decode():
            nonlocal i
            ans = ""
            while i < n and s[i] != ']':
                if s[i].isalpha():
                    ans += s[i]
                    i += 1 
                else:
                    j = s.index('[', i)
                    number = int(s[i:j])
                    i = j + 1
                    ans += number * decode()
                    
            i += 1
            return ans
        
    
        return decode()
        