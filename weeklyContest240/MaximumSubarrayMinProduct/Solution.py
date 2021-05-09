class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n = len(nums)
        # calculate prefix sum
        prefix = [0 for _ in range(n+1)]
        
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
            
        # we start from biggest value, and each time we merge intervals we visited
        nums_sorted = sorted(enumerate(nums), key=lambda x: -x[1])
        union = {} # keep track of leftmost and rightmost indices of currrent interval
    
        res = 0
        for i, val in nums_sorted:
            # check if i-1 and i+1 is in union
            l = union[i-1][0] if i-1 in union else i
            r = union[i+1][1] if i+1 in union else i
            res = max(res, (prefix[r+1] - prefix[l]) * val)
            # update union[i-1], union[i] and union[i+1]
            union[i] = [l,r]
            if i-1 in union:
                u = union[i-1][0]
                union[u][1] = r
            if i+1 in union:
                v = union[i+1][1]
                union[v][0] = l
        return res % MOD
    