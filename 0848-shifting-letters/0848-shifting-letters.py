class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = []
        
        for i in range(len(shifts)-2,-1,-1):
            shifts[i] += shifts[i+1]
      
        for i in range(len(s)):
            temp = shifts[i] + ord(s[i]) - 97
            temp %= 26
            ans.append(chr(temp + 97))
            
        return "".join(ans)
        