class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(' ')
        longest = len(max(s,key = len))
        ans = [""] * longest
        
        for i in range(len(s)):
            for _ in range(longest-len(s[i])):
                 s[i] += ' '
        for i in range(len(s)):
            for j in range(longest):
                ans[j] += s[i][j]
        for i,word in enumerate(ans):
            ans[i] = word.rstrip()

                
        return ans
        
