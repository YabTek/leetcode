class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_coming = defaultdict(int)
        order = []
        queue = deque()
        
        for a,b in prerequisites:
            graph[b].append(a)
            in_coming[a] += 1
            
        for i in range(numCourses):
            if in_coming[i] == 0:
                queue.append(i)
             
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbour in graph[node]:
                in_coming[neighbour] -= 1
                
                if in_coming[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(order) == numCourses:
            return True
        else:
            return False
        
        