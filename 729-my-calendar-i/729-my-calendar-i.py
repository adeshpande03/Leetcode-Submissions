class MyCalendar:

    def __init__(self):
        self.il = []

    def book(self, start: int, end: int) -> bool:
        c = 0
        for i in self.il:
            if start <= i[0] and end <= i[0] or start >= i[1] and end >= i[1]:
                c += 1
        if c == len(self.il):
            self.il.append((start, end))
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)