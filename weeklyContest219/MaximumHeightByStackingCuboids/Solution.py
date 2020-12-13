class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        c = list(map(sorted, cuboids))
        c.sort()
        # LIS
        dp = [0 for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                if all([c[j][k] <= c[i][k] for k in range(3)]):
                    dp[i] = max(dp[i], dp[j])
            dp[i] += c[i][2]
        return max(dp)