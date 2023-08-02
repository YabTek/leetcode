class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        ans = []
        
        while columnNumber > 0:
            columnNumber,idx = divmod(columnNumber-1, 26)
            ans = [chr(65+idx)] + ans
            
        return "".join(ans)
        