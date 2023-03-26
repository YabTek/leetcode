class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
      
        def backtrack(start,ans):
             
            if len(ans) == 4 and len(s) == start: 
                final.append(".".join(ans))
            if start == len(s):
                return    
            
            for i in range(start, len(s)):
                if int(s[start]) == 0:
                    backtrack(start+1, ans+["0"])
                    return
                elif int(s[start:i+1]) <= 255:
                    backtrack(i+1, ans+[s[start:i+1]])
                else:
                    break
        
        final = []
        backtrack(0,[])
        return final
      
