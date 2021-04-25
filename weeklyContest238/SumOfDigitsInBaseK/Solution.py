class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n>0:
            q, r = divmod(n, k)
            res += r
            n = q
        return res
    