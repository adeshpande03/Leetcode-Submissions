class Solution:
    def areSimilar(self, mat1: List[List[int]], k: int) -> bool:
        mat1 = list(map(deque, mat1))
        mat = list(map(deque, mat1))
        
        for i in range(len(mat)):
            if i % 2 == 0:
                mat[i].rotate(k)
            else:
                mat[i].rotate(-k)
        return mat == mat1