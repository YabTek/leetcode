class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        dp[0] = False
        dp[1] = False

        for i in range(2, n+1):
            for j in range(1, i//2 + 1):
                if i % j == 0 and not dp[i-j]:
                    dp[i] = True
                    break

        return dp[n]
