class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set(arr)
        for i in arr:
            if i * 2 in s:
                if i == 0:
                    if arr.count(0) > 1:
                        return True
                    else:
                        continue
                return True
            
        return False