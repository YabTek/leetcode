class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {} 
        
        for i in range(len(graph)): 
            if i not in color: 
                stack = [(i,1)]
                
                while stack: 
                    
                    node, prev_color = stack.pop()
                    
                    if node in color: 
                        if color[node] != prev_color: 
                            return False
                    else:                        
                        color[node] = prev_color 
                        for neighbour in graph[node]: 
                            stack.append((neighbour, (-1)*prev_color))              
                                
        return True
        