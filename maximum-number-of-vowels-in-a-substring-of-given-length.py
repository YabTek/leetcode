class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        ans = 0
        count = 0
        i=0
        j=0
        for j in range(len(s)):
            if j - i >= k:
                if s[i] in vowels:
                    count -= 1
                i += 1
            if s[j] in vowels:
                count += 1
            ans = max(ans, count)
            
        return ans