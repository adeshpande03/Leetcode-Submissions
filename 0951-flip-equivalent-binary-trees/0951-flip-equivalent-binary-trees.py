# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                
                flipTraversal = traverse(node1.left, node2.right) and traverse(node1.right, node2.left)
                normalTraversal = traverse(node1.left, node2.left) and traverse(node1.right, node2.right)

                return flipTraversal or normalTraversal
            
            return node1 is None and node2 is None
        
        return traverse(root1, root2)