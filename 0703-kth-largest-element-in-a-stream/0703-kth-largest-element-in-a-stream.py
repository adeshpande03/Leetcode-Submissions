class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = list(sorted(nums))
        self.k = k

    def add(self, val: int) -> int:
        insort(self.l, val)
        return self.l[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)