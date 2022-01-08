class Solution:
    def possibleToStamp(self, grid: List[List[int]], h: int, w: int) -> bool:
        # sub-matrix sum 
        # reference: https://leetcode.com/problems/stamping-the-grid/discuss/1675412/JavaC%2B%2BPython-Calulate-the-sub-matrix-sum-twice
        m,n = len(grid), len(grid[0])
        A = [[0 for _ in range(n+1)] for _ in range(m+1)] # count of occupied from (0,0) to (i,j)
        B = [[0 for _ in range(n)] for _ in range(m)] # B[i][j] is 1 if A[i][j] == w*h
        C = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                A[i+1][j+1] = A[i+1][j] + A[i][j+1] - A[i][j] + grid[i][j]
                if i+1 >= h and j+1 >= w:
                    if A[i + 1][j + 1] - A[i+1-h][j + 1] - A[i + 1][j+1-w] + A[i+1-h][j+1-w] == 0:
                        B[i][j] = 1 # means (i,j) can be put a stamp as right-bottom corner
                        
        # we we use C[i][j] as cumulative sum for B from (0,0) to (i,j)
        for i in range(m):
            for j in range(n):
                C[i+1][j+1] = C[i+1][j] + C[i][j+1] - C[i][j] + B[i][j]
                
        # now for each cell (i,j), check if sum of B from (i,j) to (i+h-1, j+w-1) is greater than 0, we can check from C
        for i in range(m):
            for j in range(n):
                r,c = min(i+h,m), min(j+w,n)
                if grid[i][j] == 0 and C[r][c] - C[r][j] - C[i][c] + C[i][j] == 0:
                    return False
                
        return True
    
