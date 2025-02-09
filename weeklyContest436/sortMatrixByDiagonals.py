class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for d in range(-n, n+1):
            arr = []
            # j - i = d
            for i in range(n):
                j = d + i
                if 0 <= j <n:
                    arr.append(grid[i][j])

            arr = sorted(arr)
            if d > 0:
                arr.reverse()
                
            for i in range(n):
                j = d + i
                if 0 <= j <n:
                    grid[i][j] = arr.pop()

        return grid
            
