class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [] 
        
        for i in range(n-2):
            temp = [] 
            for j in range(n-2):
                first = max(grid[i][j:j+3])
                second = max(grid[i+1][j:j+3])
                third = max(grid[i+2][j:j+3])
                temp.append(max(first,second,third))              
            ans.append(temp)  
            
        return ans      
       