class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        matrix_xor = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                matrix_xor[i][j] = matrix_xor[i-1][j] ^ matrix_xor[i][j-1] ^ matrix_xor[i-1][j-1] ^ matrix[i-1][j-1]
                
        h = [] # min heap, size k
        for i in range(1,m+1):
            for j in range(1, n+1):
                if len(h) < k:
                    heapq.heappush(h, matrix_xor[i][j])
                else:
                    if matrix_xor[i][j] > h[0]:
                        heappop(h)
                        heappush(h, matrix_xor[i][j])
                        
        return h[0]
    