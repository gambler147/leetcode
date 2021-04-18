class Solution:
    def checkPartitioning(self, s: str) -> bool:
        # dynamic programming, let dp[i][j] to be true if s[i:j+1] is a palindrome
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            
        for j in range(n):
            for i in range(j):
                # dp[i][j] = dp[i+1][j-1] if s[i]==s[j]
                if s[i] == s[j]:
                    if (i+1==j or dp[i+1][j-1]):
                        dp[i][j] = True
                    
        # check all posible partitions
        for j in range(n):
            for i in range(j):
                if dp[0][i] and dp[i+1][j] and dp[j+1][n-1]:
                    return True
        return False
    