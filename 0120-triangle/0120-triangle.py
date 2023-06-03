class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        @cache
        def dp(i,j):
            
            if i == n-1:
                return triangle[i][j]
            if i >= n:
                return 0
            
            return triangle[i][j] + min(dp(i+1,j),dp(i+1,j+1))
          
        return  dp(0,0)           
                         
                         
            
            
        