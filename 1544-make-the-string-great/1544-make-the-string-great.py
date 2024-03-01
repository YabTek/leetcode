class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        n = len(s)
        
        for i in range(n):
            cur = s[i]
            if stk and (cur.upper() == stk[-1].upper() and (cur.isupper() and stk[-1].islower() or cur.islower() and stk[-1].isupper())):
                stk.pop()
            else:
                stk.append(cur)
                
        return "".join(stk)
            
        
            
        
            
       
        