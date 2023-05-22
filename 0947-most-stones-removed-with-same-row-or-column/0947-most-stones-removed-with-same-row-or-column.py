class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        store = set()
        n = len(stones)
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            parent.setdefault(x,x)
            parent.setdefault(y,y)
            
            xrep = find(x)
            yrep = find(y)
        
            parent[yrep] = xrep
        
            
        for x,y in stones:
            union(x,~y)
            
        for num in parent:
            store.add(find(num))
            
        return n-len(store)
