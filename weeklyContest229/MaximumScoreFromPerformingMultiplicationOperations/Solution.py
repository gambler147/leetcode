class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # dp, O(m**2)
        n, m = len(nums), len(multipliers)
        
        dp = [[0 for _ in range(m)] for _ in range(m)]
        
        for k in range(1, m+1):
            # k is number of remaining operations
            for i in range(m-k+1):
                # i is number of operations performed on the left end of nums
                j = m - k - i # number of operations performed on the right end of nums
                if k == 1:
                    dp[i][j] = max(nums[i]*multipliers[-k], nums[-j-1]*multipliers[-k])
                else:
                    dp[i][j] = max(nums[i]*multipliers[-k]+dp[i+1][j], nums[-j-1]*multipliers[-k]+dp[i][j+1])
        return dp[0][0]
            
        