# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            nonlocal ans
            
            if not node:
                return 0
                
            goleft = traverse(node.left)
            goright = traverse(node.right)
            node.val += goleft + goright
            
            ans += abs(node.val-1)
            
            return node.val-1
            
        ans = 0
        traverse(root)
        
        return ans
            
        