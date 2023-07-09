class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        
        for i in range(2,numRows+1):
            dp=[1]*i
            for j in range(1,i-1):
                dp[j] = ans[i-2][j] + ans[i-2][j-1]
                
            ans += [dp]
            
        return ans
        