class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        queue = deque([[0,0,"color"]])
        visited = set((0,"color"))
        ans = [-1] * n
        
        redEdge = defaultdict(list)
        blueEdge = defaultdict(list)
        
        for a,b in redEdges:
            redEdge[a].append(b)
        for a,b in blueEdges:
            blueEdge[a].append(b)
            
        while queue:
            lst = queue.popleft()
            
            node = lst[0]
            len_ = lst[1]
            color = lst[2]
            
            if ans[node] == -1:
                ans[node] = len_
            
            if color != "red":
                for neighbour in redEdge[node]:
                    if (neighbour,"red") not in visited:
                        visited.add((neighbour,"red"))
                        queue.append([neighbour,len_ + 1,"red"])
            if color != "blue":
                for neighbour in blueEdge[node]:
                    if (neighbour,"blue") not in visited:
                        visited.add((neighbour,"blue"))
                        queue.append([neighbour,len_ + 1,"blue"])
                        
        return ans
                
            
                        
        
        
        
        
        