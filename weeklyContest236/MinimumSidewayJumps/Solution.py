class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # backwards dp solution
        n = len(obstacles)
        dp = [[float('inf') for _ in range(3)] for _ in range(n)] + [[0,0,0]]
        # end condition
        for i in range(n-1,-1,-1):
            o = obstacles[i]-1
            if o == -1:
                for j in range(3):
                    dp[i][j] = min(dp[i+1][j], 1+dp[i+1][(j+1)%3], 1+dp[i+1][(j+2)%3])
            else:
                dp[i][(o+1)%3] = min(dp[i+1][(o+1)%3], 1+dp[i+1][(o+2)%3])
                dp[i][(o+2)%3] = min(dp[i+1][(o+2)%3], 1+dp[i+1][(o+1)%3])
                
        # print(dp)
        return dp[0][1]
        