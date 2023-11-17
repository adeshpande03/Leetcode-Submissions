class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = dict()
        for i,j in enumerate(nums):
            if j:
                self.d[i] = j
    def dotProduct(self, vec: 'SparseVector') -> int:
        s = 0
        for i in self.d:
            if i in vec.d:
                s += self.d[i]*vec.d[i]
        return s
