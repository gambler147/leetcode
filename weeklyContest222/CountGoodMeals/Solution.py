class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # hash map
        MOD = 10**9+7
        seen = {} 
        res = 0
        for d in deliciousness:
            # for each mask = 1 << i count number of (mask - d) in dict
            for i in range(23):
                target = 1 << i
                res = (res + seen.get(target - d, 0)) % MOD
            seen[d] = seen.get(d, 0)+1
        return res
    