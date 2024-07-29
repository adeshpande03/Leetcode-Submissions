class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp, comp = [1.0] * (len(prob)+1), [1-p for p in prob]
        for i in range(len(prob)):
            dp[i+1] = dp[i]*comp[i]
        for i in range(target):
            dp[i], prev = 0, dp[i]
            for j in range(i, len(prob)):
                dp[j+1], prev = dp[j]*comp[j]+prev*prob[j], dp[j+1]
        return dp[-1]