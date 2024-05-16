# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def evaluateTree(node):
            if node.val == 2:
                return evaluateTree(node.left) or evaluateTree(node.right)
            elif node.val == 3:
                return evaluateTree(node.left) and evaluateTree(node.right)
            else:
                return node.val
        return evaluateTree(root)