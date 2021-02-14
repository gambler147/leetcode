class Solution:
    def countHomogenous(self, s: str) -> int:
        # count consecutive occurence of same character, let's say d times
        # the the number of homogenous substrings consisting of these d characters
        # is nchoosek(d+1,2)
        from math import comb
        
        MOD = 10**9+7
        res = 0
        cnt = 1 # s[0]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                res += comb(cnt+1, 2)
                cnt = 1
        res += comb(cnt+1, 2)
        return res%MOD
    