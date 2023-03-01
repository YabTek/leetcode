class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            ans =  [1]*(rowIndex + 1)
            row_before = self.getRow(rowIndex-1)
            
            for i in range(len(ans)-2):
                ans[i+1] = row_before[i] + row_before[i+1]
                
            return ans

       
      
        
        