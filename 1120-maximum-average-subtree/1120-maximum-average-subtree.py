# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max = float('-inf')
        def dfs(root):
            if not root:
                return (0, 0)
            left, nl = dfs(root.left)
            right, nr = dfs(root.right)
            avg = (left + right + root.val)/(nl + nr + 1)
            self.max = max(self.max, avg)
            return (left + right + root.val, nl + nr + 1)
        dfs(root)
        return self.max
