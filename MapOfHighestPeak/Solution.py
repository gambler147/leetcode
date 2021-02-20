class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # greedy, bfs,
        # start from water cells, expand 
        m, n = len(isWater), len(isWater[0])
        
        heights = [[None for _ in range(n)] for _ in range(m)]
        
        # start with water cells
        queue = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    heights[i][j] = 0
                    queue.append((i,j))
        
        while queue:
            tmp = []
            for i,j in queue:
                # go through 4 neighbors of (i,j)
                for p,q in [(-1,0),(1,0),(0,1),(0,-1)]:
                    x,y = i+p, j+q
                    # check if (x,y) has been visited
                    if x < 0 or x >= m or y < 0 or y >= n or heights[x][y] != None:
                        continue
                    
                    heights[x][y] = heights[i][j]+1
                    tmp.append((x,y))
            queue = tmp
        return heights
                