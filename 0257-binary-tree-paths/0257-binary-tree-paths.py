# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def traverse(node,ans):
            if not node:
                return 
            ans += str(node.val) 
          
            if (not node.left) and (not node.right):
                final.append(ans)
                return
          
            traverse(node.left, ans + "->" )
            traverse(node.right, ans + "->")
          
        
        final = []
        traverse(root, "")
        return final
    
    
        