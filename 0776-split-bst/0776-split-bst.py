# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        def BST(root, target):
            # base case
            if not root:
                return None, None

            if root.val > target:
                left, right = BST(root.left, target)

                root.left = right

                return left, root

            else:
                left, right = BST(root.right, target)
                root.right = left
                return root, right
            

        leftTree, rightTree = BST(root, target)
        ans = [leftTree, rightTree]
        return ans