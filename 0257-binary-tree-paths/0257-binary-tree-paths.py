class Solution():
    def binaryTreePaths(self, root):
        res = []
        
        def dfs(node, s):
            if s != "":
                s += "->"
            s += str(node.val)
            if not node.left and not node.right: res.append(s)
            if node.left: dfs(node.left, s)
            if node.right: dfs(node.right, s)
        dfs(root, "") 
        return res