class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [None] * n
        part_of_cycle = set()
        all_nodes = {i for i in range(n)}
             
                
        def dfs(node):
            if color[node]:
                if color[node] == "unsafe":
                    return True
                else:
                    return  False
            
            color[node] = "unsafe"
            
            for neighbour in graph[node]:
                if dfs(neighbour):
                    return True
                
            color[node] = "safe"
            return False
        
            
            
        for i in range(n):
            if dfs(i):
                part_of_cycle.add(i)
                
        
        return  sorted(all_nodes-part_of_cycle)
            
            
            
                
        
        