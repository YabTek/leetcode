# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
       
        def check(leftNode,rightNode):
            if not leftNode and not rightNode:
                return True
            if not leftNode and rightNode:
                return False
            if leftNode and not rightNode:
                return False
            if leftNode.val != rightNode.val:
                return False
            
            return check(leftNode.left,rightNode.right) and check(leftNode.right,rightNode.left)
        
        return check(root.left,root.right)
            
    
        