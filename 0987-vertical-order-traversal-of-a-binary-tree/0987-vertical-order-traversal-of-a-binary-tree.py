# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traverse(root,row,col):
            if not root:
                return 
            d[col].append((row,root.val))
            traverse(root.left,row+1,col-1)
            traverse(root.right,row+1,col+1)
           
            return d
            
            
        row = 0
        col = 0
        result = []
        d = defaultdict(list)
        ans = traverse(root,row,col)
        lst = sorted(ans.items())
        final = []
        
        for col,node in lst:
            node.sort()
            result.append(node)
        for lst in result:
            temp = []
            for pair in lst:
                temp.append(pair[1])
            final.append(temp)
        
        return final
        