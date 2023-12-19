class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = []
        for y in range(len(img)):
            temp = []
            for x in range(len(img[y])):
                t = 0
                c = 0
                for ys in [y - 1, y, y + 1]:
                    for xs in [x - 1, x, x + 1]:
                        if 0 <= ys < len(img) and 0 <= xs < len(img[0]):
                            t += (img[ys][xs])
                            c += 1
                temp.append(t//c)
            ans.append(temp)
        return ans
            
                            
                