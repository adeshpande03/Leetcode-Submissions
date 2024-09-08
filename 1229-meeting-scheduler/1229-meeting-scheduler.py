class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        n, m = len(slots1), len(slots2)
        i, j = 0, 0
        while i < n and j < m:
            a, b = slots1[i]
            x, y = slots2[j]
            diff = max(0, min(b, y)-max(a, x))
            if diff >= duration:
                return (max(a, x), max(a, x)+duration)
            if b > y:
                j += 1
            else:
                i += 1
        return []