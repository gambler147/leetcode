class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # just loop and update direction of each ball downwards
        m = len(grid)
        n = len(grid[0])
        res = []
        for c in range(n):
            i,j = 0, c # position of ball
            for _ in range(m):
                if grid[i][j] == 1:
                    # right diagonal
                    if j + 1 >= n or grid[i][j+1] == -1:
                        res.append(-1)
                        break
                    else:
                        i+=1
                        j+=1
                else:
                    # left diagonal
                    if j-1 < 0 or grid[i][j-1] == 1:
                        res.append(-1)
                        break
                    else:
                        i+=1
                        j-=1
            else:
                res.append(j)
        return res
            