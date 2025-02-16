class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def dp(i, j, h, v, turn):
            """
            i, j is cell location
            h, v, is moving direction
            turn is if we had a turn or not
            """
            val = grid[i][j]
            # 1. no turn. move to next cell
            next_i, next_j = i+h, j+v
            res = 1
            if 0 <= next_i < m and 0 <= next_j < n:
                next_val = grid[next_i][next_j]
                if (val, next_val) in [(0, 2), (2,0)]:
                    res = max(res, 1+dp(next_i, next_j, h, v, turn))
            
            # 2. make a turn
            if turn == 1:
                nxt_h, nxt_v = v, -h
                next_i, next_j = i + nxt_h, j+nxt_v
                if 0 <= next_i < m and 0 <= next_j < n:
                    next_val = grid[next_i][next_j]
                    if (val, next_val) in [(0, 2), (2, 0)]:
                        res = max(res, 1+dp(next_i, next_j,nxt_h, nxt_v, 0))

            return res

        res = 0
        dirs = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, 1)
                    for h,v in dirs:
                        next_i, next_j = i+h, j+v
                        if 0<=next_i<m and 0<=next_j<n and grid[next_i][next_j] == 2:
                            res = max(res, 1 + dp(next_i, next_j, h,v,1))
        return res
