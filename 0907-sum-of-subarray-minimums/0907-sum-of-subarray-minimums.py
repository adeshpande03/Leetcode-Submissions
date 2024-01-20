class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [-math.inf] + A + [-math.inf]
        n = len(A)

        st = []
        res = 0

        for i in range(n):
            while st and A[st[-1]] > A[i]:
                mid = st.pop()
                left = st[-1]
                right = i

                res += A[mid] * (mid - left) * (right - mid)

            st.append(i)
        return res % (10**9 + 7)
