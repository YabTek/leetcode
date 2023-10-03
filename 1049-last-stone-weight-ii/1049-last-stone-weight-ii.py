class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = {}
        
        total = sum(stones)
        half = total//2 
        
        def backtrack(cur_sum,idx):
            
            if idx == n or cur_sum >= half:
                diff = cur_sum - (total - cur_sum)
                return abs(diff)
            
            if cur_sum not in dp:
                dp[cur_sum] = min(backtrack(cur_sum+stones[idx] ,idx+1),backtrack(cur_sum,idx+1))
                
            return dp[cur_sum]
        
        return backtrack(0,0)
       