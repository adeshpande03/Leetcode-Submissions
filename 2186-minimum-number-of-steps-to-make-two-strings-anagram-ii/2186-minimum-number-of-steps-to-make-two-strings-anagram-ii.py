class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        return sum((s_counter - t_counter).values()) + sum((t_counter - s_counter).values())