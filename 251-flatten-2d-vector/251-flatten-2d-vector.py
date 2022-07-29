class Vector2D:

    def __init__(self, vec: List[List[int]]):
        il = []
        for i in vec:
            for j in i:
                il.append(j)
        self.il = il
        self.id = -1

    def next(self) -> int:
        self.id += 1
        return self.il[self.id]

    def hasNext(self) -> bool:
        return True if self.id + 1 < len(self.il) else False
        
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()