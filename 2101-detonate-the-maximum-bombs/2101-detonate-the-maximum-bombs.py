class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
       
        n = len(bombs)
        ans = 0
        graph = defaultdict(list)
        
        def hasGreaterRadius(i,j):
            x1 = bombs[i][0]
            x2 = bombs[j][0]
            y1 = bombs[i][1]
            y2 = bombs[j][1]
            
            radius = bombs[i][2]
            
            if radius >= math.sqrt((x1-x2)**2 + (y1-y2)**2):
                return True
 
        for i in range(n):
            for j in range(n):
                if i != j and hasGreaterRadius(i,j):
                    graph[i].append(j)
      
    
        def dfs(node):
            
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
                            
        for i in range(n):
            visited = set()
            dfs(i)
            ans = max(ans,len(visited))

                          
        return ans
        
        
        