class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        nums = [i for i in range(1, n+1)]
        allowed = list(set(nums) - set(banned))
        allowed.sort()
        
        ans = 0
        tot = 0
        
        for i in range(len(allowed)):
            tot += allowed[i]
            if tot > maxSum:
                return ans
            ans += 1

            
        return ans 
        