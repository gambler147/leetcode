class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # simply count number of plants between every pair of 2 seats O(n)
        n = len(corridor)
        seats = []
        for i in range(n):
            if corridor[i] == 'S':
                seats.append(i)
        # seats must be even
        s = len(seats)
        if s == 0 or s%2 == 1:
            return 0
        
        MOD = 10**9+7
        res = 1
        for i in range(1, s-1, 2):
            res = (res * (seats[i+1]-seats[i]))%MOD
        
        return res
    
