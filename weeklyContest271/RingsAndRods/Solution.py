class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)//2
        cnts = [set() for _ in range(10)]
        for i in range(n):
            cnts[int(rings[2*i+1])].add(rings[2*i])
            
        res = 0
        for i in range(10):
            res += int(len(cnts[i]) == 3)
        return res
    
