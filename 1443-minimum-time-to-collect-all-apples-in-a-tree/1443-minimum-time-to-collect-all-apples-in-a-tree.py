class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set()
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(node):
            
            ans = 0 
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    time = dfs(neighbour)
                    if time or hasApple[neighbour]:
                        ans += time + 2
                        
            return ans
                    
        return dfs(0)
            
        
        