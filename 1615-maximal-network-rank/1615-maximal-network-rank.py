class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        graph = defaultdict(list)
        
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        
        for i in range(n):
            for j in range(i + 1, n):
                graph[i] = set(graph[i])
                rank = len(graph[i]) + len(set(graph[j]))
                if j in graph[i]:
                    rank -= 1
                ans = max(ans, rank)
        
        return ans
       
            
    
        