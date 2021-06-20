class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # dfs, return true if current cell is a valid candidate of a subisland and all other cells in
        # the same island are valid subisland
        res = 0
        m,n = len(grid1), len(grid1[0])
        
        def dfs(i,j):
            # if current cell of grid2 is 0 or '*', it is not a valid candidate
            if grid2[i][j] != 1:
                return 0
            
            ans = True
            # mark i,j as *
            grid2[i][j] = '*'
            # if cell is not a island cell in grid1, it is not a valid subisland candidate for grid2
            if grid1[i][j] != 1: ans = False
            # visit i,j's neighbors
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x,y = i+dx, j+dy
                # we only visit neighbors that are 1s
                if 0<=x<m and 0<=y<n and grid2[x][y] == 1:
                    ans &= dfs(x,y)
            return ans
        
        # loop through all cells
        for i in range(m):
            for j in range(n):
                res += dfs(i,j)
        
        return res
        
                
            