# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def bfs(root):
            q = [root]
            level = 1
            while q:
                for _ in range(len(q)):
                    node = q.pop(0)
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                    if not (node.right or node.left):
                        return level
                level += 1
            return level
        return bfs(root)
                    
            