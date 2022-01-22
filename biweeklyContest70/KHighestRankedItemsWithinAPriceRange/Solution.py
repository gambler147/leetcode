class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        # min heap of size k
        # and BFS for distance
        m,n = len(grid), len(grid[0])
        i0, j0 = start
        low, high = pricing
        h = [] # min-heap of cells
        visited = set() # visited cells
        
        bfs = [(i0, j0)]
        visited.add((i0,j0))
        dist = 0
        while bfs:
            tmp = []
            for i,j in bfs:
                # add current point to heap
                if low <= grid[i][j] <= high:
                    heapq.heappush(h, (dist, grid[i][j], i, j))
                    
                # get all its neighbors
                for ci,cj in [(-1,0),(0,-1),(1,0),(0,1)]:
                    x, y = i+ci, j+cj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != 0 and (x,y) not in visited:
                        tmp.append((x,y))
                        visited.add((x,y))
            bfs = tmp
            dist += 1
            
        # recover top k heap
        res = []
        while h and len(res) < k:
            dist, val, i,j = heapq.heappop(h)
            res.append([i,j])
            
        return res
    
