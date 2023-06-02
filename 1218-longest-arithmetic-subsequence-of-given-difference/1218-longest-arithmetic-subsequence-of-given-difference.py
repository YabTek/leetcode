class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        
        for i in range(n):
            diff = arr[i]-difference
            if diff not in dp:
                dp[arr[i]] = 1
            else:
                dp[arr[i]] = dp[diff]+1
        
        dp = sorted(dp.values())
        
        return dp[-1]
                
            
        