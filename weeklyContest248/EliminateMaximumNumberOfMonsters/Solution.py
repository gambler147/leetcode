class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = sorted([d/s for (d,s) in zip(dist, speed)])
        res = 0
        for i,t in enumerate(times):
            if t <= i:
                return res
            res += 1
        return res
            
