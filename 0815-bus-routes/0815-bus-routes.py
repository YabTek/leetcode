class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        buses = 0
        graph = defaultdict(list)
        queue = deque([source])
        visited = set([source])
        visited_bus = set()
        
        
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                graph[routes[i][j]].append(i)
                
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                
                if node == target:
                    return buses
                
                for bus in graph[node]:
                    if bus not in visited_bus:
                        visited_bus.add(bus)

                        for sequence in routes[bus]:
                            if sequence not in visited:
                                visited.add(sequence)
                                queue.append(sequence)

            buses += 1
                            
        return -1

                    
                    
                    
                    
        