class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        parent = {i : i for i in range(n)}
        rank = [0]*n
        store = []
        
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
                parent[yrep] = xrep
                rank[xrep] += 1
                
        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                store.append([dist,i,j])
        
        count = 0
        for dist,i,j in sorted(store):
            if find(i) != find(j):
                union(i,j)
                ans += dist
                count += 1
                if count == n-1:
                    return ans
        return ans         
