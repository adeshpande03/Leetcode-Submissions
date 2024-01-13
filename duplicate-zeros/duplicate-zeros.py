class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        s = ''.join([str(i) for i in arr]).replace('0','00')[0:len(arr)]
        arr[0:len(arr)] = [int(i) for i in list(s)]