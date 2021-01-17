class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        # dp ?
        m = len(grid)
        n = len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        avail = 0
        # find initial positions of cat, mouse
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '#':
                    avail += 1
                if grid[i][j] == 'C':
                    ci,cj = i,j
                elif grid[i][j] == 'M':
                    mi,mj = i,j
        
        @functools.lru_cache(None)
        def dp(ci, cj, mi, mj, turn):
            if step == avail * 2:
                # we already search all available grids
                return False
            
            # if mouse's turn
            if step%2==0:
                # iterate four directions, with each direction a maximum
                # jump of mouseJump, stop in the direction if running into a wall
                for di, dj in dirs:
                    for jump in range(mouseJump+1):
                        x, y = mi+di*jump, mj+dj*jump
                        if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                            # valid grid cell
                            if dp(ci,cj,x,y,step+1) or grid[x][y] == 'F':
                                return True
                        else:
                            # cannot jump over the wall
                            break
                return False
            else:
                # cat's turn
                for di,dj in dirs:
                    for jump in range(catJump+1):
                        x, y = ci+di*jump, cj+dj*jump
                        if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                            # valid grid cell
                            if not dp(x,y,mi,mj,step+1) or (x,y) == (mi,mj) or grid[x][y] == 'F':
                                return False
                        else:
                            # cannot jump over the wall
                            break
                return True

        return dp(ci, cj, mi, mj, 0)
    