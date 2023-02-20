class MagicDictionary:

    def __init__(self):
        self.s = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.s = set(dictionary)

    def search(self, searchWord: str) -> bool:
        for i in self.s:
            if len(i) == len(searchWord):
                diff = 0
                for idx in range(len(searchWord)):
                    if searchWord[idx] != i[idx]:
                        diff += 1
                if diff == 1:
                    return True
        
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)