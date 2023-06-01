# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        
        def dp(node,flag):
            
            if (node,flag) in cache:
                return cache[(node,flag)]
            
            if not node:
                return 0

            if flag:
                option1 = node.val + dp(node.left,False) + dp(node.right,False)
                option2 = dp(node.left,True) + dp(node.right,True)
                cache[(node,flag)] = max(option1, option2)
                return cache[(node,flag)]
            
            cache[(node,flag)] = dp(node.left,True) + dp(node.right,True)
            return cache[(node,flag)]

            
                
                
                
        return dp(root, True)
