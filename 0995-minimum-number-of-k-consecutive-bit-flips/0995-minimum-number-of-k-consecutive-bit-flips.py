class Solution:
    def minKBitFlips(self, n: List[int], k: int) -> int:
        q,o=set(),0
        for l,v,r in zip(count(),n,count(k-1)):
            if (1-v+len(q))%2:
                o+=1
                q.add(r)
            q.discard(l)#if i in q:q.remove(i)
        return -1 if q else o