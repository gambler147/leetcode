class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        from functools import lru_cache
        n = len(s)
        char_loc = {}
        for i,char in enumerate(s):
            if char not in char_loc:
                char_loc[char] = [i, i]
            else:
                char_loc[char][1] = i
                
        @lru_cache(None)
        def dp(i, k):
            # forming k disjoint special substring starting from index i
            if k == 0:
                return True

            if i >= n:
                return False
            # determine if we want to include
            char = s[i]
            min_idx, max_idx = char_loc[char]
            if min_idx < i:
                canMakeSpecial = False
            else:
                # iterate through
                idx = i
                while idx <= max_idx:
                    nxt_char = s[idx]
                    nxt_min_idx, nxt_max_idx = char_loc[nxt_char]
                    if nxt_min_idx < i or (i == 0 and max_idx == n-1):
                        canMakeSpecial = False
                        break
                    max_idx = max(max_idx, nxt_max_idx )
                    idx += 1

                if idx > max_idx:
                    canMakeSpecial = dp(idx, k-1)
            
            return dp(i+1, k) or canMakeSpecial

        return dp(0, k)

