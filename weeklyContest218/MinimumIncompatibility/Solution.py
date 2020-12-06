class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        # dynamic programming? 
        n = len(nums)
        group_size = n//k  
        incomp = {}
                
        # pre calculation
        for mask in range(1, 2**n):
            if bin(mask).count('1') == group_size:
                res_max, res_min = -float('inf'), float('inf')
                for i in range(n):
                    if mask & (1 << i):
                        res_max = max(res_max, nums[i])
                        res_min = min(res_min, nums[i])
                incomp[mask] = res_max - res_min
                    
        @functools.lru_cache(None)
        def dp(mask):
            # return incompatibility of mask, mask has multiple of k 1s
            if mask == 0: return 0
            indices = [i for i in range(len(nums)) if mask & (1<<i)]
                    
            res = float('inf')
            # remove k indices each time
            for comb in itertools.combinations(indices, group_size):
                if len(set([nums[idx] for idx in comb])) != group_size:
                    continue
                combmask = 0
                newmask = mask
                comb_min, comb_max = float('inf'), -float('inf')
                for idx in comb:
                    combmask += 1 << idx
                    newmask ^= 1 << idx

                res = min(dp(newmask) + incomp[combmask], res)
                
            return res

        res = dp(2**n-1)
        return -1 if res == float('inf') else res