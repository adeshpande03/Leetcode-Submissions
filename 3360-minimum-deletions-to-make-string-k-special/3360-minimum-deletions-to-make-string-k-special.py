class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c=Counter(word)
        v=sorted([0]+list(c.values()))
        answ=sum(v)
        prefSum=0
        i=0
        n=len(v)
        while i<n:
            val=v[i]
            while i<n and v[i]==val:
                prefSum+=v[i]
                i+=1
            j=1
            if i<n:
                val=v[i]
            y=0
            while j<n and k<v[-j]-val:
                y+=v[-j]-val-k
                j+=1
            answ=min(answ,prefSum+y)
        return answ