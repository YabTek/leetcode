class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        ans = 0
        tot = 0
        
        for num in nums:
            tot += num
            if tot == goal:
                ans += 1
            if tot-goal in d:
                ans += d[tot-goal]
            d[tot] += 1
            
        return ans