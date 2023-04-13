class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

            
        graph = defaultdict(list)
           
        for i in range(len(isConnected)):
            row = isConnected[i]
            for j in range(len(row)):
                if row[j] == 1:
                    graph[i+1].append(j+1)
                    
        ans = 0           
        visited = set()
        
        for i in range(1,len(isConnected)+1):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans
        
        
        