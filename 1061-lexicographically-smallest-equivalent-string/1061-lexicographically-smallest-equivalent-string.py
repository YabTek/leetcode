class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        
        for i in range(26):
            char = chr(i+97)
            parent[char] = char
              
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        def union(x,y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep != yrep:
                if xrep < yrep:
                    parent[yrep] = xrep
                else:
                    parent[xrep] = yrep
                    
                    
        for a,b in zip(s1,s2):
            union(a,b)
            
        ans = []
        for char in baseStr:
            ans.append(find(char))
            
        return "".join(ans)
                    
        