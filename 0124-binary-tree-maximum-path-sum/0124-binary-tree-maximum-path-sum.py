# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left.;
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            if left < 0:
                left = 0
           
            right = dfs(node.right)
            if right < 0:
                right = 0
            
            total = node.val + left + right
            
            self.ans = max(total,self.ans)
            
            return node.val + max(left ,right)


            
        self.ans = float("-inf")
        dfs(root)
        
        return self.ans
        