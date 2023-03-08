# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def traverse(root,level = 0):
            if not root:
                return 
        
            for _ in range(len(ans),level+1):
                ans.append([])
            ans[level].append(root.val)
            
            traverse(root.left, level+1)
            traverse(root.right, level+1)
           
            return ans
     
        return traverse(root)
    
        