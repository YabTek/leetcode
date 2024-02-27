class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stk = []
        
        for char in s:
            if char not in ["(",")"]:
                continue
            elif char == "(":
                stk.append(char)
            else:
                ans = max(ans,len(stk))
                stk.pop()
                
        return ans
        