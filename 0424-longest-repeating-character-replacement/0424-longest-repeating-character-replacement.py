class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        for c in s:
             d[c] = 0
        result = 0
        j = 0
        for i in range(len(s)):
            d[s[i]]+=1
            max_  = max(d.values())
            while i-j+1 - max_ > k:
                d[s[j]]-= 1
                j+=1
            result = max(result,i-j+1)
        return result
        