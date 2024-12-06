class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ans = 0
        tot = 0
        
        for num in range(1, n + 1):
            if num not in banned:
                tot += num 
                if tot > maxSum:
                    return ans
                ans += 1

        return ans 
        