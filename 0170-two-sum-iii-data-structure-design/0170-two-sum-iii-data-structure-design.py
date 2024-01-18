class TwoSum:

    def __init__(self):
        self.nums = defaultdict(int)

    def add(self, number: int) -> None:
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        for i in self.nums:
            if self.nums.get(value - i, 0):
                if i == value - i and self.nums.get(i) == 1:
                    continue
                return True
            


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)