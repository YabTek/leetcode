class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        ans = 0
        
        for char in s:
            if char == "(":
                stk.append(char)
            else:
                if not stk:
                    ans += 1
                else:
                    stk.pop()
                    
        return ans + len(stk)
                
                
            
        