# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        ans = []
        queue = deque([[target,0]])
        
        def buildGraph(node):
            
            if not node:
                return
            
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                buildGraph(node.left)
                
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                buildGraph(node.right)
                
        buildGraph(root)
        visited.add(target)
        
        while queue:
            node,dist = queue.popleft()
            
            if dist == k:
                ans.append(node.val)
                
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append([neighbour,dist+1])
                    
        return ans
                
        
        
        
        