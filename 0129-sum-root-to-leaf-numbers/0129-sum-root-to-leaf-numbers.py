class Solution:
    def sumNumbers(self, n: Optional[TreeNode]) -> int:
        def f(n, q):
            if n:
                q = 10 * q + n.val
                if result := f(n.left, q) + f(n.right, q):
                    return result

                return q

            return 0

        return f(n, 0)
