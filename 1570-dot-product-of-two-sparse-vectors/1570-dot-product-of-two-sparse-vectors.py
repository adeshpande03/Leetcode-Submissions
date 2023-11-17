class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = dict()
        for i,j in enumerate(nums):
            if j:
                self.d[i] = j
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        s = 0
        for i in self.d:
            if i in vec.d:
                s += self.d[i]*vec.d[i]
        return s

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)