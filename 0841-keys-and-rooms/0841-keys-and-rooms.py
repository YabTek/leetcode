class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for i in range(len(rooms)):
            graph[i] = rooms[i]
            
        def dfs(node):
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
                    
        visited = set()
        dfs(0)
        for i in range(len(rooms)):
            if i not in visited:
                return False
        return True
                    
                
        