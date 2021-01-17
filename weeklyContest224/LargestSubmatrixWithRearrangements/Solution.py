class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # prefix sum
        m = len(matrix)
        n = len(matrix[0])
        prefix = [[0 for _ in range(n)] for _ in range(m)]
        # initialize
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                prefix[i][j] = prefix[i-1][j] + 1
                
        # for each row sort and find maximum area
        res = 0
        for r in prefix:
            r.sort()
            for i in range(n):
                res = max(res, r[i] * (n-i))
        return res
    