"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        def dfs(id):
            visited.add(id)
            
            ans = importance[id]
            for neighbour in graph[id]:
                if neighbour not in visited:
                    ans += dfs(neighbour)
                    
            return ans
        
        graph = defaultdict(list)
        importance = defaultdict(int)
        visited = set()
        
        for node in employees:
            importance[node.id] = node.importance
            graph[node.id] = node.subordinates

        return dfs(id)
        
                
                    
                    
            
            
       