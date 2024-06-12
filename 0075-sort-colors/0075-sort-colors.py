class Solution:
    def sortColors(self, a: List[int]) -> None:
        for i in range(len(a)):
            m = i
            for j in range(i + 1, len(a)):
                if a[j] < a[m]:
                    m = j
            a[m], a[i] = a[i], a[m]
        
