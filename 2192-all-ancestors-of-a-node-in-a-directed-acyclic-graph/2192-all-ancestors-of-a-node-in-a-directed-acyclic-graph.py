class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_coming = defaultdict(int)
        queue = deque()
        ans = [set() for _ in range(n)]
        
        
        for a,b in edges:
            graph[a].append(b)
            in_coming[b] += 1
            
        for i in range(n):
            if in_coming[i] == 0:
                queue.append(i)
       
        
        while queue:
            node = queue.popleft()
            
            for neighbour in graph[node]:
                in_coming[neighbour] -= 1
                
                ans[neighbour].add(node)
                ans[neighbour] = ans[neighbour].union(ans[node])
                    
                if in_coming[neighbour] == 0:
                    queue.append(neighbour)
                    
        for i in range(len(ans)):
            ans[i] = sorted(ans[i])
           
            
                    
        return ans
            
        
        
            
        
        