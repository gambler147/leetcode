class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        # if word1 and word2 have no common chars, return 0
        if len(set(word1).intersection(set(word2))) == 0:
            return 0

        # find longest palindrome subsequence of word1 + word2
        # but only when left index is in word1 and right index is in word2 
        # we update our result
        m, n = len(word1), len(word2)
        s = word1 + word2
        dp = [[0 for _ in range(m+n)] for _ in range(m+n)]

        for i in range(m+n):
            dp[i][i] = 1
            
        res = 0
        for cl in range(2, m+n+1):
            # length of subarray
            for i in range(m+n-cl+1):
                j = i+cl-1
                if s[i] == s[j]:
                    if j == i+1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                
                    # only update our result when left index lies in word1 and 
                    # right index lied in word2
                    if i < m and j >= m:
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                
        return res
    