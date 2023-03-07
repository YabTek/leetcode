# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        return Solution.traverse(root,ans)
    
    def traverse(node,ans):
        if not node:
            return node
        Solution.traverse(node.left,ans)
        ans.append(node.val)
        Solution.traverse(node.right,ans)
        
        return ans
            
       
        