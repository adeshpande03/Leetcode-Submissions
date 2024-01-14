class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def helper(num,i):
            t=num//(2**i)
            ans=t*(2**(i-1))
            num=num%(2**i)
            ans=ans+max(0,num-2**(i-1)+1)
            return ans
        
        start=0
        end=(2**60)  
        ans=0
        while start<=end:
            curr=0
            mid=(start+end)//2
            for i in range(x,60,x):
                curr+=helper(mid,i)
            if curr<=k:
                ans=max(ans,mid)
                start=mid+1
            else:
                end=mid-1
        return ans