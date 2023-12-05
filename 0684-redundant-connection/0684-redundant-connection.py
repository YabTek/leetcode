class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
     
        self.rep = {i:i for i in range(1,len(edges)+1)}

        def representative(x):
            while x != self.rep[x]:
                x = self.rep[x]
            return x

        def union(x, y):
            nonlocal ans
            
            xrep = representative(x)
            yrep = representative(y)
            
            if xrep == yrep:
                ans = [x,y]
            self.rep[yrep] = xrep
            
            return ans


        ans = []
        
        for a,b in edges:
            union(a,b)
            
            
        return ans



