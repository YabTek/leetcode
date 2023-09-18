# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def traverse(node,depth,parent):
            if not node:
                return 
            d[node.val] = [depth,parent]
            traverse(node.left,depth+1,node.val)
            traverse(node.right,depth+1,node.val)
            
        d = defaultdict(list)  
        traverse(root,0,None)
        
        return d[x][0] == d[y][0] and d[x][1] != d[y][1]
            
            
            
            
            

            
        