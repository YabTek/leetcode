# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(node,tot):
            if not node:
                return 
            
            tot += node.val
            if not node.left and not node.right and tot == targetSum:
                return True
            return traverse(node.left,tot) or traverse(node.right,tot)
        
        return traverse(root,0)
        