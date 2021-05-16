class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        Standard dynamic programming solution. Time: O(nk). Space: O(nk)
        
        Explanation:
        
        Given n and k, let dp(n,k) be the solution. Consider 2 cases:
        1. place stick with length 1 leftmost; the first stick is visible, then all remaining sticks are longer than
            the first stick, so we need to arrange the remaining n-1 sticks such that exactly k-1 are visible, 
            which is exactly dp(n-1, k-1)
        2. place any stick except length 1 leftmost; in this case, length-1 stick is never visible. Total number of ways
            to arrange the n-1 stick except length-1 stick to make k visible is dp(n-1, k). Then we insert the length-1
            stick to the right of any of the n-1 sticks, which is dp(n-1, k) * (n-1)
            
        so dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j-1]
        """
        MOD = 10**9+7
        
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        # initialize
        dp[1][1] = 1
        for i in range(2, n+1):
            for j in range(1, min(k+1, i+1)):
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] * (i-1)) % MOD
        return dp[n][k]
        