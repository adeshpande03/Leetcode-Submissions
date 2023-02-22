class Solution:
    def topKFrequent(self, il: List[int], k: int) -> List[int]:
        d = {}
        for i in il:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        thing = [(d[i], i) for i in (d)]
        thing.sort(reverse = True)
        thing = thing[0:k]
        print(thing)
        return [i[1] for i in thing]



            