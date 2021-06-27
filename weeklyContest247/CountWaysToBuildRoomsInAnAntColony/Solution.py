class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        # top-bottom dp
        from math import factorial
        n = len(prevRoom)
        MOD = 10**9+7
        childs = collections.defaultdict(list)
        for i, j in enumerate(prevRoom):
            if j!=-1:
                childs[j].append(i)
                
        # precalculate factorial modulo and inverse factorial modulo
        f = [1,1]
        f_inv = [1,1]
        for i in range(2, n+1):
            f.append(f[-1]*i%MOD)
            f_inv.append((pow(i,-1,MOD) * f_inv[-1]) % MOD)
            
        @functools.lru_cache(None)
        def num_childs(r):
            ans = 1
            for c in childs[r]:
                ans += num_childs(c)
            return ans
            
        @functools.lru_cache(None)
        def dp(r):
            # return total number of ways to build rest of rooms starting from r
            nc = num_childs(r) - 1
            ans = f[nc]
            for c in childs[r]:
                ans = (ans * dp(c) * f_inv[num_childs(c)]) % MOD
            return ans % MOD
        
        return dp(0)
        
            
            