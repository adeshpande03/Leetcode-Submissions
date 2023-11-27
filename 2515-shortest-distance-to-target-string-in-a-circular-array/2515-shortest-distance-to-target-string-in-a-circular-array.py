class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        res = inf
        for index,value in enumerate(words):
            if value == target:
                res = min(res, (min(abs(index-startIndex), (abs(len(words)-abs(index-startIndex))))))
                  
        return (res)