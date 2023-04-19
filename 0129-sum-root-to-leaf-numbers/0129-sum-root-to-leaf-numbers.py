# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,num):
            if not node:
                return
            num += str(node.val)
            dfs(node.left,num)
            dfs(node.right,num)
            
            if not node.right and not node.left:
                self.total += int(num)
                
            return self.total
        
        self.total = 0
        
        return dfs(root,"")
        
            
        