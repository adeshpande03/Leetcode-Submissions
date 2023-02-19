# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def bfs(root):
            res = []
            q = [root]
            rev = True
            while q:
                curr = []
                for i in range(len(q)):
                    node = q.pop(0)
                    curr.append(node.val)
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                if True:
                    curr.reverse()
                res.append(curr)
            return res
        return reversed((bfs(root)))
                
        