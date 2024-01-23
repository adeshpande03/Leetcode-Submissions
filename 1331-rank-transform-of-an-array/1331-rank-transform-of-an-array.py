class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank_dict = {value: index + 1 for index, value in enumerate(sorted_arr)}
        
        result = [rank_dict[num] for num in arr]
        return result