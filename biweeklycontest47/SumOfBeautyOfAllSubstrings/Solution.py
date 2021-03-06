class Solution:
    def beautySum(self, s: str) -> int:
        # sliding window O(26*n**2)
        n = len(s)
        res = 0
        for w in range(1,n+1): # window size
            cntr = collections.Counter()
            # initialize
            for i in range(w):
                cntr[s[i]] += 1
            res += max(cntr.values()) - min(cntr.values())
            for i in range(w, n):
                cntr[s[i]] += 1
                cntr[s[i-w]] -= 1
                if cntr[s[i-w]] == 0:
                    del cntr[s[i-w]]
                res += max(cntr.values()) - min(cntr.values())
        return res
                
    