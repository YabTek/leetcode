class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans = []
        graph = defaultdict(list)
        
        for i,(a,b) in enumerate(equations):
            graph[a].append((b,values[i]))
            graph[b].append((a,1/values[i]))

       
        for a,b in queries:
            queue = [(a,1)]
            if a not in graph:
                ans.append(-1)
                continue
                
            flag = False
            visited = set([a])
            
            while queue:
                node,cur_weight = queue.pop()
                    
                if node == b:
                    flag =  True
                    ans.append(cur_weight)
                    break
                    
                for neighbour,weight in graph[node]:
                    if neighbour  not in visited:
                        queue.append((neighbour,weight * cur_weight))
                        visited.add(neighbour)
                    
                    
            if not flag :
                ans.append(-1)
                   
        return ans
                    
                
            
            
        
        
        