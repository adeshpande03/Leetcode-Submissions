class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        he = heights[:]
        c = 0
        h = 1
        while h:
            h = 0
            for i in range(len(heights) - 1):
                if heights[i + 1] < heights[i]:
                    h = 1
                    heights[i], heights[i + 1] = heights[i + 1], heights[i]
        for i in range(len(he)):
            if he[i] != heights[i]:
                c += 1
        return c
        print(heights)