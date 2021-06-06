class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # brute force; rotate 4 times, each 90 degrees, and check if mat == target
        def rotate(matrix):
            # rotate matrix 90 degree clockwise
            return list(zip(*matrix[::-1]))
        
        def equal(m1, m2):
            m, n = len(m1), len(m1[0])
            ans = [m1[i][j] == m2[i][j] for i in range(m) for j in range(n)]
            return all(ans)
        
        m = len(mat)
        n = len(mat[0])
        mat_ = [[mat[i][j] for j in range(n)] for i in range(m)]
        
        for _ in range(4):
            mat_ = rotate(mat_)
            if equal(target, mat_):
                return True
        return False

        