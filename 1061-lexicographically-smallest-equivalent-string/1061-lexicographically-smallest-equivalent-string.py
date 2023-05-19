class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
    
        def find(x):
            
            if x != parent[x]:
                parent[x]  = find(parent[x])
            return parent[x]
            
        def union(x,y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep == yrep:
                return 
            elif xrep < yrep:
                parent[yrep] = xrep
            else:
                parent[xrep] = yrep
           
            
        ans = ""  
        parent = {}
        
        for i in range(26):
            char = chr(i+97)
            parent[char] = char
             
        for a,b in zip(s1,s2):
            if a == b:
                continue
            union(a,b)
            
        for char in baseStr:
            ans += find(char)
            
        return ans
        
        
        