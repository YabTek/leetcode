class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = []
        ans = []
        opened = 0
        closed = 0
        
        for char in s:
            if char == "(":
                opened += 1
            elif char == ")":
                closed += 1
            if opened == closed:
                ans.append("".join(stk[1:]))
                opened = 0
                closed = 0
                stk = []
                continue
            stk.append(char)
                
        return "".join(ans)
                
        