class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        def backtrack(start):
            nonlocal final
            
            if start >= len(cookies):
                return max(ans)                
         
            for i in range(k):
                ans[i] += cookies[start]
                if ans[i] >= final:
                    ans[i] -= cookies[start]
                    continue  
                final = min(final,backtrack(start+1))
                ans[i] -= cookies[start]
            
            return final 
                
        final = inf
        ans = [0]*k
        return backtrack(0)
     
        