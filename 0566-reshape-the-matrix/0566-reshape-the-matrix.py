class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        list1,matrix=list(chain.from_iterable(mat)),[]
        if len(mat)*len(mat[0])!=r*c:
            return mat
        for i in range(0,len(list1),c):
            matrix.append(list1[i:i+c])
        return matrix