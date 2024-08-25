# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node):
            if node == None:
                return []

            if node.left == None and node.right == None:
                return [node.val]
            return postorder(node.left) + postorder(node.right) + [node.val]
        return postorder(root)