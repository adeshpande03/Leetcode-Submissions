class Solution:
    def knightDialer(self, n: int) -> int:
        num_map = {0:[4,6], 
                   1:[8,6], 
                   2:[7,9], 
                   3:[4,8], 
                   4:[3,0,9], 
                   5:[], 
                   6:[1,7,0], 
                   7:[2,6], 
                   8:[1,3], 
                   9:[4,2]}
        MOD = 10**9 + 7
        dp = [0] * 10
        prev = [1] * 10
        
        for r in range(1,n):
            dp = [0] * 10
            for s in range(10):
                ans = 0
                for nsq in num_map[s]:
                    ans = (ans + prev[nsq]) % MOD
                dp[s] = ans
            prev = dp
            
        ans = 0
        for square in range(10):
            ans = (ans + prev[square])
        return ans % MOD
            
            
        
        
            