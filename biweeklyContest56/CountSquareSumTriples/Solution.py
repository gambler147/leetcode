class Solution:
    def countTriples(self, n: int) -> int:
        from math import sqrt
        res = 0
        squares = set([i**2 for i in range(1, n+1)])
        for i in range(2, n):
            for j in range(2, n):
                if i**2 + j**2 in squares:
                    res += 1
        return res
    
                    