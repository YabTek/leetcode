class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        
        if m > len(haystack):
            return -1
        
        num = 26 + 1
        pattern1 = 0
        pattern2 = 0
        
        for char in needle:
            m -= 1
            pattern1 += num**m * ((ord(char) - 97) + 1)
            
        m = len(needle)  
        for i in range(m):
            m -= 1
            pattern2 += num**m * ((ord(haystack[i]) - 97) + 1)
            
        if pattern1 == pattern2:
            return 0
        
        n = len(needle)-1
        j = 0
        
        for i in range(len(needle),len(haystack)):
            pattern2 -= num**n * ((ord(haystack[j])-97)+1) 
            pattern2 *= num
            pattern2 += num**0 * ((ord(haystack[i])-97) + 1)
            
            if pattern2 == pattern1:
                return j+1
            else:
                j += 1
                
        return -1
            
            
       
        