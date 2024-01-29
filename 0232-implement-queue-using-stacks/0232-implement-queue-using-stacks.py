class MyQueue:

    def __init__(self):
        self.il = []
        self.temp = 0

    def push(self, x: int) -> None:
        self.il.append(x)
        

    def pop(self) -> int:
        self.x = self.il[0]
        self.il.pop(0)
        return self.x
        

    def peek(self) -> int:
        return self.il[0]

    def empty(self) -> bool:
        return len(self.il) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()