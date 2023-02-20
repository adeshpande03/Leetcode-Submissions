# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            if not root:
                return
            res = []
            q = [root]
            while q:
                level = []
                for _ in range(len(q)):
                    node = q.pop(0)
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                    level.append(node.val)
                res.append(level)
            return res
        traversed = bfs(root)

        odds = [traversed[i] for i in range(len(traversed)) if i % 2 == 0]
        
        evens = [traversed[i] for i in range(len(traversed)) if i % 2 == 1]
        print(odds)
        print(evens)
        print(traversed)
        for i in odds:
            if len(set(i)) != len(i):
                return False
            if i != list(sorted(i, reverse = True)):
                return False
            if sum([n % 2 for n in i]) != len(i):
                return False
        for i in evens:
            if len(set(i)) != len(i):
                return False
            if i != list(sorted(i)):
                return False
            if sum([n % 2 for n in i]) != 0:
                return False
            
        return True
        
                    
                    
            