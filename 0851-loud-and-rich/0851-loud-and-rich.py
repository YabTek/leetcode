class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        ans = [i for i in range(n)]
        graph = defaultdict(list)
        in_coming = defaultdict(int)
        queue = deque()
        
        
        for a,b in richer:
            graph[a].append(b)
            in_coming[b] += 1
            
        for i in range(n):
            if in_coming[i] == 0:
                queue.append(i)
                ans[i] = i
                
        while queue:
            node = queue.popleft()
            
            for neighbour in graph[node]:
                in_coming[neighbour] -= 1
                
                if quiet[ans[node]] < quiet[ans[neighbour]]:
                    ans[neighbour] = ans[node]
                    quiet[neighbour] = ans[neighbour]
                
                
                if in_coming[neighbour] == 0:
                    queue.append(neighbour)
            
        return ans
        
        
        