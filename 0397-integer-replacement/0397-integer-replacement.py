class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}  

        def dp(num):
            if num == 1:  
                return 0
            if num in memo:  
                return memo[num]

            if num % 2 == 0:  
                memo[num] = dp(num // 2) + 1
            else:
                memo[num] = min(dp(num + 1), dp(num - 1)) + 1  

            return memo[num]

        return dp(n)
        