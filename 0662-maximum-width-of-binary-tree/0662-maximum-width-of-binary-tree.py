# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        que = deque([(root, 0)])
        
        while que:
            ans = max(ans, que[-1][1] - que[0][1])
            
            for _ in range(len(que)):
                node, temp = que.popleft()
                
                if node.left:
                    que.append((node.left, temp * 2 - 1))
                if node.right:
                    que.append((node.right, temp * 2))
                    
        return ans + 1
        