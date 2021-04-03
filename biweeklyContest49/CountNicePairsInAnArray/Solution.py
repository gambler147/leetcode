class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # precompute rev array and using hashmap to for nums[i] - rev[i]
        n = len(nums)
        MOD = 10**9+7
        rev = [int(str(a)[::-1]) for a in nums]
        mp = collections.Counter()
        
        res = 0
        for i in range(n):
            cur = nums[i] - rev[i]
            if cur in mp:
                res = (res + mp[cur]) % MOD
            mp[cur] += 1
        return res
                