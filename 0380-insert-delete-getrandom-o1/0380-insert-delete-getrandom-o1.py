class RandomizedSet:
    def __init__(self):
        self.rSet = {}
        self.rSet2 = {}
        self.ind = 0

    def insert(self, val: int) -> bool:
        if val in self.rSet2:
            return False
        self.rSet[self.ind] = val
        self.rSet2[val] = self.ind
        self.ind += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.rSet2:
            rInd = self.rSet2[val]
            self.rSet2.pop(val)
            self.rSet.pop(rInd)
            return True
        return False

    def getRandom(self) -> int:
        chosen = random.randint(0, self.ind)
        while chosen not in self.rSet:
            chosen = random.randint(0, self.ind)
        return self.rSet[chosen]
