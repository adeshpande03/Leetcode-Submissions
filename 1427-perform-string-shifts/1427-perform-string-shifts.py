class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s = deque(list(s))
        for g in shift:
            if g[0] == 0:
                s.rotate(-1 * g[1])
            else:
                s.rotate(g[1])
        return ''.join(list(s))