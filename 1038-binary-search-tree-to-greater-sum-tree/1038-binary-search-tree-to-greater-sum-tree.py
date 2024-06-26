# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum = [0]
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            node.val += sum[0]
            sum[0] = node.val
            dfs(node.left)
        dfs(root)
        return root
#if you upvote this you get a good job offer in a week