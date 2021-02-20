class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # brute force O(n^3)
        n = len(s)
        res = 0
        res_i,res_j = -1, -1
        for i in range(n):
            for j in range(i+1, n+1):
                sub = set(s[i:j])
                for c in sub:
                    if c.swapcase() not in sub:
                        break
                else:
                    if j-i > res:
                        res = max(res, j-i)
                        res_i, res_j = i, j
        return s[res_i:res_j]
    