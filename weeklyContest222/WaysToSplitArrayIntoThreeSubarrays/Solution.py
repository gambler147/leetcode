class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        # binary search?
        # iterate i from 0 to n-3, find smallest j such that si <= sj - si
        # and biggest j such that sj - si <= sn-1 - sj
        MOD = 10**9+7
        n = len(nums)
        s = [0 for _ in range(n)]
        cur = 0
        # prefix sum
        for i in range(n):
            cur += nums[i]
            s[i] = cur
        res = 0
        for i in range(n-2):
            j_small = max(bisect.bisect_left(s, 2*s[i]), i+1)
            j_big = min(bisect.bisect_right(s, (s[i] + s[n-1])/2), n-1)
            # print(j_small)
            # print(j_big)
            if j_small <= j_big:
                res = (res + j_big - j_small) % MOD
        return res
        