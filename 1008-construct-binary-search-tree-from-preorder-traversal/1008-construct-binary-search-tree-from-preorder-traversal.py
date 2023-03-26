# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def binaryTree(node,num):
            if not node:
                node = TreeNode(num)
                return node
            
            if num < node.val:
                node.left = binaryTree(node.left,num)
            else:
                node.right = binaryTree(node.right,num)

            return node
        
       
        root = TreeNode(preorder[0])
        for num in preorder[1:]:
            binaryTree(root,num)
        return root
           
        