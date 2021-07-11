class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9+7
        def is_valid(cur, prev):
            for c, p in zip(cur, prev):
                if c == p:
                    return False
            return True
        
        @functools.lru_cache(None)
        def valid_paints_generator(m):
            # return default valid paints
            COLOR = 3
            res = []
            def dfs(cur):
                if len(cur) == m:
                    res.append(tuple(cur))
                    return
                for c in range(COLOR):
                    if len(cur)==0 or cur[-1] != c:
                        cur.append(c)
                        dfs(cur)
                        cur.pop()
            
            dfs([])
            return res
            
            
        @functools.lru_cache(None)
        def next_valid_col_paints(prev_col):
            # given previous column painting, return list of all possible paitings for next column
            # there are in total 3**m possible combinations 
            # time complexity for this function is O(3**m).
            # This function is cached and will be called for 3**m times (for each combination) so total
            # time complexity is O(9**m) and space O(9**m)
            m = len(prev_col)
            
            res = []
            for paint in valid_paints_generator(m):
                if is_valid(paint, prev_col):
                    res.append(tuple(paint))
            return res
        
        @functools.lru_cache(None)
        def dp(valid_paint, i):
            # return number of possible paints given current paint
            if i == n:
                return 1
            
            res = 0
            for paint in next_valid_col_paints(valid_paint):
                res = (res + dp(paint, i+1)) % MOD
            return res
        
        return dp(tuple([-1]*m), 0)
            
