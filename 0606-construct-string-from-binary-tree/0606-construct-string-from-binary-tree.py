# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            
            ans = []
            
            if not node: 
                return ""

            ans.append(str(node.val))
            
            if not node.left and not node.right:
                 return "".join(ans)
                
            ans.append("(" + str(dfs(node.left)) + ")")
            
            if node.right:
                ans.append("(" + str(dfs(node.right)) + ")")
                
            return "".join(ans)

            
        return dfs(root)
