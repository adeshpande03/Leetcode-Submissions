class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s = set()
        i = 0
        while True:
            if arr[i] not in s:
                s.add(i)
                i += 1
                if i >= len(arr):
                    return ''
                if i == k:
                    return arr[i]
            else:
                i +=1
            if i >= len(arr):
                return ''
        return ''            
        