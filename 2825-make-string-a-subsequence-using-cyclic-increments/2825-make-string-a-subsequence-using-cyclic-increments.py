class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0  
        n, m = len(str1), len(str2)

        while i < n and j < m:
            char1 = str1[i]
            char2 = str2[j]
            
            if (char1 == char2) or (char1 == 'z' and char2 == 'a') or (ord(char1) == ord(char2) - 1):
                j += 1
            i += 1
            
        return j == m