class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        queue = deque()
        ans = []
        
        for a,b in prerequisites:
            graph[b].append(a)
            incoming[a] += 1
            
        for i in range(numCourses):
             if incoming[i] == 0:
                queue.append(i)
           
                
        while queue:
            course = queue.popleft()
            ans.append(course)
            
            for neighbour in graph[course]:
        
                incoming[neighbour] -= 1
                
                if incoming[neighbour] == 0:
                    queue.append(neighbour)

        if len(ans) != numCourses:
            return []
        return ans      
        