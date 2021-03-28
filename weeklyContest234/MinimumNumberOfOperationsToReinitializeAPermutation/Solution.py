class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # notice the mapping for index is i -> 2*i mod (n-1)
        # we just need to find k, such that 2**k mod (n-1) = 1 (identity)
        res = 0
        i = 1
        while (res == 0 or i > 1):
            i = i*2 % (n-1)
            res += 1
        return res
        