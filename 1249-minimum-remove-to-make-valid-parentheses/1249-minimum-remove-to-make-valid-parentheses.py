class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        n = len(s)
        s = list(s)
        
        for i in range(n):
            if s[i] == "(":
                stk.append(i)
            if s[i] == ")":
                if stk and s[stk[-1]] == "(":
                    stk.pop()
                else:
                    stk.append(i)
                    
        for i in stk:
            s[i] =""
                
        return "".join(s)
                
        