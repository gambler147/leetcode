class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        # iterate all possible values x of GCD (1 ~ max(nums))
        # x is gcd if and only if there are multiples of x in nums and
        # gcd of all these multiples are x
        T = max(nums)+1 
        nset = set(nums)
        res = 0
        
        for x in range(1, T):
            g = 0
            for y in range(x, T, x):
                if y in nset:
                    g = self.gcd(g, y)
                if g == x:
                    # if we already have gcd of the first multiples of x, we found
                    # a subsequence whose gcd is x
                    res+=1
                    break
        return res
            
    def gcd(self, a, b):
        if a==0: return b
        if b==0: return a
        a, b = min(a,b), max(a,b)
        while a > 1:
            q, r = divmod(b, a)
            if r == 0:
                return a
            a,b = r,a
        return a
        