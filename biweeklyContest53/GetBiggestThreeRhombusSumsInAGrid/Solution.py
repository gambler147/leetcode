class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # maintain two diagonal prefix sum. Iterate each cell and expand the side length from 0 to max
        # calculate diagonal sum for four sides and add in a set. Return largest 3 elements in the set.
        # Time complexity O(mn*min(m,n)), Space: O(mn)
        
        m, n = len(grid), len(grid[0])
        prefix_rd = [[0 for _ in range(n)] for _ in range(m)]
        prefix_ld = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                prefix_rd[i][j] = prefix_rd[i-1][j-1] + grid[i][j] if i-1 >= 0 and j-1 >= 0 else grid[i][j]
                prefix_ld[i][j] = prefix_ld[i-1][j+1] + grid[i][j] if i-1 >= 0 and j+1 < n else grid[i][j]
        s = set()
        # loop for each top corner
        for i in range(m):
            for j in range(n):
                # loop for all possible side length
                for k in range(min(m, n)):
                    if i + 2*k >= m or j+k >= n or j-k < 0:
                        break
                    if k == 0:
                        rhombus = grid[i][j]
                    else:
                        rhombus = prefix_rd[i+k][j+k] - prefix_rd[i-1][j-1] if i-1 >= 0 and j-1>=0 else prefix_rd[i+k][j+k]
                        rhombus += prefix_rd[i+2*k][j] - prefix_rd[i+k][j-k]
                        rhombus += prefix_ld[i+k][j-k] - prefix_ld[i][j]
                        rhombus += prefix_ld[i+2*k-1][j+1] - prefix_ld[i+k][j+k]
                    # put rhombus to set
                    s.add(rhombus)
        res = []
        for _ in range(3):
            if s:
                m = max(s)
                res.append(m)
                s.remove(m)
        return res
                    
                    