class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = {i : i for i in range(n)}
        groups = defaultdict(list)
        ans = ""
        rank = [0] * n
        
        if len(pairs) == 0:
            return s
        
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xrep = find(x)
            yrep = find(y)
            
            if rank[xrep] > rank[yrep]:
                parent[yrep] = xrep
            elif rank[yrep] > rank[xrep]:
                parent[xrep] = yrep
            else:
                parent[xrep] = yrep
                rank[xrep] += 1
                
                     
        for a,b in pairs:
            union(a,b)
            
        for i in range(n):
            groups[find(i)].append(s[i])   
        
        for key in groups:
            groups[key].sort(reverse = True)
        
        for j in range(n):
            ans += groups[find(j)].pop()
            
        return ans
