class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)-1
        maxi,prev = arr[n],0
        arr[n] = -1
        while n:
            n = n-1
            maxi = max(prev,maxi)
            prev = arr[n]
            arr[n] = maxi
        return arr