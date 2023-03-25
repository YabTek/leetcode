# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def findSum(node,preSum):
            nonlocal ans
            
            if not node:
                return 0
            curSum = preSum + node.val  
            if curSum == targetSum:
                ans += 1
            if curSum - targetSum in d:
                ans += d[curSum - targetSum]
            d[curSum] += 1
            
            findSum(node.left,curSum)
            findSum(node.right,curSum)
          
            d[curSum] -= 1
            
            return ans        
         
        ans = 0
        d = defaultdict(int)
        
        return findSum(root,0)
      
        
            