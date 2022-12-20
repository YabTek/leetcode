class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
            elif  (i < len(s) and s[i] != t[j]) or (j == len(t)-1) :
                return t[j]
           
            
                
        