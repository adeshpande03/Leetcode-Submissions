# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        rh = self.height(root.right)
        lh = self.height(root.left)
        if rh - lh in [-1, 0, 1] and self.isBalanced(root.right) and self.isBalanced(root.left):
            return True
        return False
            