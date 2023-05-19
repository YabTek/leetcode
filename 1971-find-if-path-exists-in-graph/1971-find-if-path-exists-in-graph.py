class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = {i : i for i in range(n)}
        
        def find(x):
            
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep == yrep:
                return
            parent[xrep] = yrep
            
        def isConnected(x,y):
            return find(x) == find(y)
            
        
        for a,b in edges:
            union(a,b)
        return isConnected(source,destination)
            
        
            
        
            
        
       