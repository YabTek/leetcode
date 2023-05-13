class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = defaultdict(int)
        graph = defaultdict(list)
        in_coming = defaultdict(int)
        ans = []
        queue = deque()
        
        if len(edges) == 0:
            return [0]
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            in_coming[a] += 1
            in_coming[b] += 1
            
        for i in range(n):
            if in_coming[i] == 1:
                queue.append(i)
                
        while n > 2:
            n -= len(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for neighbour in graph[node]:
                    in_coming[neighbour] -= 1
                    
                    if in_coming[neighbour] == 1:
                        queue.append(neighbour)
                        
        return queue
                        

            
        
            
        
       