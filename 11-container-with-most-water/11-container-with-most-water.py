class Solution:
    def maxArea(self, height: List[int]) -> int:
        il = height.copy()
        lp = 0 
        rp = len(il) - 1
        maxMum = 0
        while lp != rp:
            if min(il[lp], il[rp]) * (rp - lp) > maxMum:
                maxMum = min(il[lp], il[rp]) * (rp - lp)
            if il[lp] < il [rp]:
                lp += 1
            else:
                rp -= 1

        return maxMum
            