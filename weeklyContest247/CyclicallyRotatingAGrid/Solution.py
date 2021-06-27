class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # for each layer, rotate k % (layer size) times
        m,n = len(grid), len(grid[0])
        
        def rotate_layer(l):
            # rotate layer i, notice for layer i, width is m-2*l and length is n-2*l
            i,j = l,l
            cur = grid[i][j]
            row_move, col_move = 1, 0
            for step in range(2*(m+n-4*l)-4):
                # move i,j to next cell
                if i+row_move >= m-l:
                    row_move, col_move = 0, 1
                if i+row_move < l:
                    row_move, col_move = 0, -1
                if j+col_move >= n-l:
                    row_move, col_move = -1, 0
                if j+col_move <l:
                    row_move, col_move = 1, 0
                i, j = i+row_move, j+col_move
                tmp = grid[i][j]
                grid[i][j] = cur
                cur = tmp
            
        for l in range(min(m//2,n//2)):
            step = k % (2*(m+n-4*l) - 4)
            for _ in range(step):
                rotate_layer(l)
        
        return grid
            
                
        