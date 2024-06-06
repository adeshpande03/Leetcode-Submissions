class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        for i in sorted(c):
            if c[i]>0: 
                c_i = c[i] 
                for j in range(i,i+groupSize):
                    if c[j] < c_i: 
                        return False
                    c[j] -= c_i
        return True
