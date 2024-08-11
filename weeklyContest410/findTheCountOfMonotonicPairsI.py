class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        # find the minium arr2[i] to make arr1[i] non-decreasing
        MOD = 10**9 + 7
        
        n = len(nums)
        m = max(nums)+1
        
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0] = [1] * m

        for i in range(1, n):
            v = max(0, nums[i] - nums[i-1])
            for j in range(v, nums[i] + 1):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j-v] )% MOD

        return sum(dp[n-1]) % MOD
            

