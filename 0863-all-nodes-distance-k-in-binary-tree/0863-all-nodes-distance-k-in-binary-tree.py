# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def traverse(node, p):
            if not node:
                return

            parent[node] = p
            traverse(node.left, node)
            traverse(node.right, node)

        traverse(root, None)
        print(parent)

        que = deque([(target, 0)])
        visited = set([target])
        ans = []

        while que:
            node, dist = que.popleft()
            if dist == k:
                ans.append(node.val)
            for neighbor in (node.left, node.right, parent[node]):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    que.append((neighbor, dist + 1))

        return ans


        
        