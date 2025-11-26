class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n

        for i in range(n):
            for word in wordDict:
                k = len(word)
                if i + 1 < k:
                    continue

                if (i + 1 == k or dp[i - k]) and s[i - k + 1: i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]

        
        
        