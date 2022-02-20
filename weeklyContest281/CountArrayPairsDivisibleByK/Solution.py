class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = collections.Counter()
        divisors = []
        for i in range(1, k+1):
            if k % i == 0:
                divisors.append(i)
               
        res = 0
        for i in range(n):
            r = k // self.gcd(nums[i], k)
            res += counter[r]
            for d in divisors:
                if nums[i] % d == 0:
                    counter[d] += 1
                    
        return res
                
    def gcd(self, a, b):
        if b == 0:
            return a
        
        q, r = divmod(a, b)
        return self.gcd(b, r)
    
