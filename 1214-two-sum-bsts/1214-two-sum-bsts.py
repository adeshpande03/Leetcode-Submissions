# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(node, data):
            if node is None:
                return
            data.add(node.val)
            dfs(node.left, data)
            dfs(node.right, data)
        
        def dfs2(node, data):
            if node is None:
                return False
            if (target - node.val) in data:
                return True
            return (
                dfs2(node.left, data)
                or dfs2(node.right, data)
            )

        data = set()
        dfs(root1, data)        
        return dfs2(root2, data)