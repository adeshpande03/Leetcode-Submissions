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
                # 我的理解是，如果root.val > target，就进去root的左边找出比 target 小和大的左右子树 left 和 right
                # 因为如果root.val > target，那么其实自动就分成了 root 和 root.left 两个部分了

                root.left = right
                # 找到的right，即刚才进去root.left之后，在这里面发现的应该属于root这部分的(即: > target部分的树串)
                # 把它接到root.left

                return left, root
                # 返回分好的两颗子树，root.left(<=target and >target)

            else:
                left, right = BST(root.right, target)
                root.right = left
                return root, right
            

        leftTree, rightTree = BST(root, target)
        ans = [leftTree, rightTree]
        return ans