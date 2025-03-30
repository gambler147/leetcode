class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        # check for all substrings
        m = len(s)
        n = len(t)
        res = 0
        for i in range(m):
            for j in range(i, m+1):
                subs = s[i:j]
                for p in range(n):
                    for q in range(p, n+1):
                        subt = t[p:q]
                        temp = subs + subt
                        if temp == temp[::-1]:
                            res = max(res, len(temp))
        
        return res
