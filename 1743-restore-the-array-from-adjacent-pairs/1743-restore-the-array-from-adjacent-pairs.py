class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_coming = defaultdict(int)
        order = []
        queue = deque()
        visited = set()
        
        for a,b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            in_coming[a] += 1
            in_coming[b] += 1
            
        for a,b in in_coming.items():
            if b == 1:
                visited.add(a)
                queue.append(a)
                break
                        
           
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbour in graph[node]:
                
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
                    
        return order
            
            
    
        