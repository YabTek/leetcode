class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node,path):

            if node == destination:
                ans.append(path.copy())
                return
            for neighbour in _graph[node]:
                path.append(neighbour)
                dfs(neighbour,path)
                path.pop()

        source = 0       
        destination = len(graph)-1 
        
        _graph = defaultdict(list)
        ans = []
        
        for i in range(len(graph)):
            _graph[i] = graph[i]
                
        dfs(source,[0])
        
        return ans
        
                
            
       