class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        # rolling hash
        BASE, MOD = 10**5+1, 10**11+19
        m = len(paths)
        min_path = min(paths, key=lambda x: len(x))
        k0 = len(min_path)
        # binary search    
        l, r = 0, k0
        while l < r:
            mid = (l+r+1)>>1 # size of substrings we are looking for
            hs = set() # keep intersection of hash values of substrings
            for i in range(m):
                # if current hashset is empty for i != 0, we can skip the rest
                if i!=0 and len(hs) == 0:
                    break
                _hash, d = 0, 1
                hs_tmp = set()
                for j in range(len(paths[i])):
                    _hash = (_hash * BASE + paths[i][j]) % MOD
                    if j >= mid:
                        _hash = (MOD + _hash - d*paths[i][j-mid]%MOD)%MOD
                    else:
                        d = d*BASE%MOD
                    if (j>=mid-1 and (i==0 or _hash in hs)):
                        hs_tmp.add(_hash)
                hs = hs_tmp
            if not hs:
                r = mid-1
            else:
                l = mid
        return l
            