class Solution:
    def minSwaps(self, data: List[int]) -> int:
        oneNums = sum(data)
        n = len(data)
        if oneNums < 2:
            return 0

        ## use the number of one as a window size
        cur = 0
        for i in range(oneNums):
            cur += data[i]
        #print(cur)

        max_one = cur
        for i in range(oneNums, n):
            cur += data[i]
            cur -= data[i-oneNums]
            max_one = max(max_one, cur)

        return (oneNums-max_one)
        