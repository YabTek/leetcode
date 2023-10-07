class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = len(queries)
        ans = [False] * n
        heap = []
        graph = defaultdict(list)
        incoming = defaultdict(int)
        order = {i : set() for i in range(numCourses) }
        
        for a,b in prerequisites:
            graph[a].append(b)
            incoming[b] += 1
        
        for i in range(numCourses):
            if incoming[i] == 0:
                heapq.heappush(heap,i)
        
                
        while heap:
            node = heapq.heappop(heap)

            for neighbour in graph[node]:
                incoming[neighbour] -= 1
                
                order[neighbour] |= ((order[node]).union({node}))
                
                if incoming[neighbour]  == 0:
                    heapq.heappush(heap,neighbour)
        
        for i in range(n):
            if queries[i][0] in order[queries[i][1]]:
                ans[i] = True
                       
        return ans
                    
                
                
        