class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
     
        self.rep = {i:i for i in range(1,len(edges)+1)}

        def representative(x):
            while x != self.rep[x]:
                x = self.rep[x]
            return x

        def union(x, y):
            xrep = representative(x)
            yrep = representative(y)
            
            if xrep == yrep:
                return [x,y]
            self.rep[yrep] = xrep

        ans = 0
        
        for a,b in edges:
            ans = union(a,b)
            if ans:
                return ans
            
        return ans



