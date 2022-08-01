class SmallestInfiniteSet:

    def __init__(self):
        self.il = list(range(1,1001))

    def popSmallest(self) -> int:
        x = self.il[0]
        self.il.pop(0)
        return x

    def addBack(self, num: int) -> None:
        if num not in self.il:
            self.il.append(num)
            self.il.sort()


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)