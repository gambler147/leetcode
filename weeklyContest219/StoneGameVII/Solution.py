class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        # dp(i,j) is the maximum difference starting with alice
        # first calculate prefix sum
        n = len(stones)
        prefix = [0]
        cur = 0
        for s in stones:
            cur += s
            prefix.append(cur)
            
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            for i in range(j-1, -1,-1):
                dp[i][j] = max(prefix[j+1]-prefix[i+1] - dp[i+1][j], prefix[j]-prefix[i] - dp[i][j-1])

        return dp[0][n-1]