class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [1] * 10
        
        directions = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
      

        for _ in range(n - 1):
            new_ = [0] * 10
            for i in range(10):
                for move in directions[i]:
                    new_[move] += dp[i]
                    new_[move] %= mod
            dp = new_

        return sum(dp) % mod

