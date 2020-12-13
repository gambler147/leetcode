class Solution:
    def minPartitions(self, n: str) -> int:
        # largest digit
        res = 0
        for c in n:
            res = max(res, int(c))
        return res