class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = collections.deque([(root, root.val)])
        while queue:
            node, val = queue.popleft()
            if not node.left and not node.right:
                if val == targetSum: return True
                else: continue
            if node.left:
                queue.append((node.left, val + node.left.val))   
            if node.right:
                queue.append((node.right, val + node.right.val))   
        return False