# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left.;
#         self.right = right

class ThroneInheritance:
    
    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.kingName = kingName
        self.visited = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName) 
    def death(self, name: str) -> None:
        self.visited.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        ans = []
        
        def dfs(node):
            if node not in self.visited:
                ans.append(node)
            for child in self.graph[node]:
                dfs(child)
                
        dfs(self.kingName)
        return ans
                
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()