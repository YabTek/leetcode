class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        
        for i in range(n-2,-1,-1):
            min_ = inf
            for j in range(1,nums[i]+1):
                jump = j+i
                
                if jump >= n-1:
                    dp[i] = 1   
                elif dp[jump] == 0 or dp[jump] == None:
                    continue
                else:
                    min_ =  min(min_,1+dp[jump])
                    dp[i] = min_
         
        return dp[0]
        