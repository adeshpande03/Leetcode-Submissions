class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        max_freq = max(count.values())
        matrix = [[] for _ in range(max_freq)]
        i = 0
        for num, freq in count.items():
            for _ in range(freq):
                matrix[i].append(num)
                i = (i+1)%len(matrix)
        return matrix        
