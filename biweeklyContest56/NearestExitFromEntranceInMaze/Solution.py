class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        
        def isBorder(i,j):
            return [i,j] != entrance and (i in (0, m-1) or j in (0, n-1))
        
        
        # use bfs O(mn)
        queue = [entrance]
        maze[entrance[0]][entrance[1]] = '+'
        res = 0
        while queue:
            tmp = []
            for i,j in queue:
                if isBorder(i,j):
                    return res
                # append its neighbor 
                for x,y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<=x<m and 0<=y<n and maze[x][y] == '.':
                        tmp.append([x,y])
                        # mark as visited
                        maze[x][y] = '+'
            res += 1
            queue = tmp
        return -1
    
