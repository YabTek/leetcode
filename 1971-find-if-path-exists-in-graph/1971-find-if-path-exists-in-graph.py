class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set([source])
        stk = [source]
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        while stk:
            node = stk.pop()
            if node == destination:
                return True
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stk.append(neighbour)
                    visited.add(neighbour)
        return False

       