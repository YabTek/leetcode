class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        color = {}
        
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
            
        for i  in range(1,n):
            if i not in color:
                stk = [(i,1)]
                while stk:
                    node,prev_color = stk.pop()
                    
                    if node in color:
                        if color[node] != prev_color:
                            return False
                    else:  
                        color[node] = prev_color
                        for neighbour in graph[node]:
                            stk.append((neighbour,(-1)*prev_color))
                        
        return True
                        
            
            
            
        