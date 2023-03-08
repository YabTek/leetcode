# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(root,level = 0):
            if not root:
                return 
        
            for _ in range(len(store),level+1):
                store.append([])
            store[level].append(root.val)
            
            traverse(root.left, level+1)
            traverse(root.right, level+1)
                    
            return store
        
        ans = []
        store = []           
        nodes = traverse(root)
        
        if nodes:
            for node in nodes:
                    if len(node) == 1:
                        ans.append(node[0])
                    else:
                        ans.append(node[-1])
                        
        return ans
    
        