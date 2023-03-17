# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
      
        def traverse(node):
            nonlocal count
            
            if not node:
                return (0,0)
            
            left = traverse(node.left)
            right = traverse(node.right)

            total = left[0] + node.val + right[0]
            cnt = left[1] + right[1] + 1
            avg = total // cnt

            if avg == node.val:
                count += 1
                
            return total, cnt
          
        count = 0
        traverse(root)
        return count