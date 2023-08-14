class Solution:
    def mostVisited(self, n, A):
        return range(A[0], A[-1] + 1) if A[0] <= A[-1] else list(range(1, A[-1] + 1)) + list(range(A[0], n + 1))