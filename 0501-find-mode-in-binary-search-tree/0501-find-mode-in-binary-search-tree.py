# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        ans = []

        
        def traverse(node):
            if not node:
                return 
            d[node.val] += 1
            traverse(node.left)
            traverse(node.right)
            
            return d
        
        max_ = max(traverse(root).values())
        for node,count in d.items():
            if count == max_:
                ans.append(node)
        return ans
        
        