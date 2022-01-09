class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # brute force and use set
        # O(mn)
        n = len(matrix)
        # check row
        for i in range(n):
            if len(set(matrix[i])) != n:
                return False
        # check col
        for j in range(n):
            if len(set([matrix[i][j] for i in range(n)])) != n:
                return False
        return True
    
