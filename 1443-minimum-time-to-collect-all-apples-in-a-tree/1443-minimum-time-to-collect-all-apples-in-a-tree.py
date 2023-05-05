class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set()
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(node):
            
            time = 0 
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    temp = dfs(neighbour)
                    if temp or hasApple[neighbour]:
                        time += temp + 2
                        
            return time
                    
        return dfs(0)
            
        
        