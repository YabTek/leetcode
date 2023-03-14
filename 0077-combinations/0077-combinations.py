class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(left,ans):
            if len(ans) == k:
                final.append(ans.copy())
                
            for num in range(left,n+1):
                ans.append(num)
                backtrack(num+1,ans)
                ans.pop()
                
            return final
         
        final = []
        return  backtrack(1,[])
     
