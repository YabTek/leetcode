class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set([0])
        
        while queue:
            node = queue.popleft()
            
            for keys in rooms[node]:
                if keys not in visited:
                    queue.append(keys)
                    visited.add(keys)
        
        for i in range(len(rooms)):
            if i not in visited:
                return False
            
        return True
                    
                
            
        