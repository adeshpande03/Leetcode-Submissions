# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def equalToDescendants(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        count = [0]

        def helper(node):
            if node.left == None and node.right == None:
                if node.val == 0:
                    count[0] += 1
                return node.val
            lv = 0
            rv = 0
            if node.left:
                lv = helper(node.left)
            if node.right:
                rv = helper(node.right)
            # print("node.val =", node.val)
            # print("lv =", lv)
            # print("rv =", rv)
            if node.val == lv + rv:
                # print("$$")
                count[0] += 1
            return node.val + lv + rv

        helper(root)

        # print("Count[0]=",count[0])
        return count[0]
