class Solution:
    def repeatedCharacter(self, s: str) -> str:   
        d = {} 
        
        for i, char in enumerate(s):
            if char not in d:
                d[char] = i
            else:
                return char

        