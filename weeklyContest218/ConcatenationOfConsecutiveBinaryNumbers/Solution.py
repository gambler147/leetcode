class Solution:
    def concatenatedBinary(self, n: int) -> int:
        from math import floor, log2
        MOD = 10**9 + 7
        res = 0
        for i in range(1, n+1):
            # number of digits of binary representation of i is math.floor(log(i))+1
            d = int(floor(log2(i))) + 1
            res = (res * (1<<d) + i) % MOD
            
        return res