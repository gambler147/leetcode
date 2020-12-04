class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        # backtracking
        matrix = [[0 for _ in range(n)] for _ in range(m)] # 1 is intro 2 is extro 0 is unoccupied
    
        res = 0
        def dfs(i, j, intro, extro, score):
            nonlocal res
            # 3 cases: empty, intro or extro
            if j == n:
                i += 1
                j = 0
            
            if i >= m: 
                res = max(res, score)
                return
            
            if intro == 0 and extro == 0:
                res = max(res, score)
            
            if score + 120 * intro + 160 * extro < res:
                # pruning, if the score for remaining intros and extros cannot exceed we current optimal score, we stop
                return
            
            ans = score
            if intro > 0:
                tmp = score + 120
                matrix[i][j] = 1
                tmp += adjust_score(i, j, i-1, j) + adjust_score(i,j,i,j-1)
                dfs(i, j+1, intro-1, extro, tmp)
                matrix[i][j] = 0
                
            if extro > 0:
                tmp = score + 40
                matrix[i][j] = 2
                tmp += adjust_score(i, j, i-1, j) + adjust_score(i,j,i,j-1)
                dfs(i, j+1, intro, extro-1, tmp)
                matrix[i][j] = 0
                
            if ((i-1 >= 0 and matrix[i-1][j] > 0) or (j-1>=0 and matrix[i][j-1] > 0)):
                dfs(i, j+1, intro, extro, score)
                
                
            
        def adjust_score(i1, j1, i2, j2):
            if 0 <= i1 < m and 0 <= i2 <m and 0<=j1<n and 0<=j2<n:
                if matrix[i1][j1] == 0 or matrix[i2][j2] == 0:
                    return 0
                s = set([matrix[i1][j1], matrix[i2][j2]])
                if s == set([1]):
                    return -60
                elif s == set([2]):
                    return 40
                else:
                    return -10
            else:
                return 0
            
        dfs(0, 0, introvertsCount, extrovertsCount, 0)
        return res
                
            
