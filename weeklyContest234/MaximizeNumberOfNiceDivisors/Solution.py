class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        # problem is : max Prod(r1,..rk), s.t. Sum(r1,...rk) <= primeFactors
        MOD = 10**9+7
        if primeFactors == 1:
            return 1
        elif primeFactors == 2:
            return 2
        
        q, r = divmod(primeFactors, 3)
        if r == 1:
            return pow(3, q-1, MOD) * 4 % MOD
        elif r == 2:
            return pow(3, q, MOD) * 2 % MOD
        else:
            return pow(3, q, MOD)
        
    