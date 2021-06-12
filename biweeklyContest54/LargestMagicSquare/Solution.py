class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        """
        store prefix row, prefix col, prefix diagonal and sub-diagonal matrix.
        Then loop for each cell in grid, expand its size until maximum, check if 
        matrix's rows, cols and diags sum are equal.
        
        Time complexity O(mn*min(m,n)), space complexity O(mn)
        """
        m, n = len(grid), len(grid[0])
        prow = [[0 for _ in range(n+1)] for _ in range(m+1)]
        pcol = [[0 for _ in range(n+1)] for _ in range(m+1)]
        pmaindiag = [[0 for _ in range(n+1)] for _ in range(m+1)]
        psubdiag = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                prow[i][j] = prow[i][j-1] + grid[i][j]
                pcol[i][j] = pcol[i-1][j] + grid[i][j]
                pmaindiag[i][j] = pmaindiag[i-1][j-1] + grid[i][j]
                psubdiag[i][j] = psubdiag[i-1][j+1] + grid[i][j]
                
        def ismagic(i, j, k):
            # determine if (i,j) -> (i+k, j+k) is a magic matrix
            s = set()
            for row in range(i, i+k+1):
                s.add(prow[row][j+k] - prow[row][j-1])
            for col in range(j, j+k+1):
                s.add(pcol[i+k][col] - pcol[i-1][col])
            s.add(pmaindiag[i+k][j+k] - pmaindiag[i-1][j-1])
            s.add(psubdiag[i+k][j] - psubdiag[i-1][j+k+1])
            return len(s) == 1
        
        res = 0
        # loop for all position starting point
        for i in range(m):
            for j in range(n):
                # size of matrix can be 1 to min(m, n) if the i+k < m and j+k < n
                for k in range(min(m-i, n-j)):
                    # check if prefix sum are same for 
                    if ismagic(i,j,k):
                        res = max(res, k+1)
        return res
                    
        