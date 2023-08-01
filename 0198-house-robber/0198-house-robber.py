class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #top-down
        #d = {}
        #def dp(idx):
            #if idx == 0:
                #return nums[0]
            #if idx < 0:
                #return 0
            #if idx not in d:
                #d[idx] =  max(nums[idx] + dp(idx-2), dp(idx-1))
                
            #return d[idx]
            
        #return dp(len(nums)-1)
        
        #bottm-up
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = nums
        dp[1] = max(dp[0],dp[1])
        
        
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i] + dp[i-2])
            
        return dp[-1]
        
        
       
            
            
        