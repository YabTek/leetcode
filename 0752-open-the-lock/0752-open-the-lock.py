class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def graph(node):
            neighbours = []
            
            for i in range(len(node)):
                choices = [node[:i] + str((int(node[i])+1) % 10) + node[i+1:], node[:i] + str((int(node[i])-1+10) % 10) + node[i+1:]]
                neighbours += choices
                
            return neighbours
            
            
        def bfs(start):
            queue = deque([(start,0)])
            
            while queue:
                node,ans = queue.popleft()
                
                if node == target:
                    return ans
                for neighbour in graph(node):
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour,ans + 1))
                        
            return -1
    
        visited = set(deadends)
        
        return bfs("0000") if "0000" not in visited else -1
        