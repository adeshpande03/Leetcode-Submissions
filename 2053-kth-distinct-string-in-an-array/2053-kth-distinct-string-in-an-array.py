class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)   # stores {ch: freq}
        count = 0
        for num in arr:
            if dict(counter)[num] == 1:
                count += 1

                # stop; found a solution
                if count == k:
                    return num
        
        return ''