class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        for i in range(26):
            char = chr(i+97)
            parent[char] = char
            
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep != yrep:
                if xrep < yrep:
                    parent[yrep] = xrep
                else:
                    parent[xrep] = yrep
                
          
        for a,b,c,d in equations:
            if b == "=":
                union(a,d)
         
        ans = True
        for a,b,c,d in equations:
            if b == "!" and find(a) == find(d):
                ans = False
                
            
        return ans
                
            
                
            
        