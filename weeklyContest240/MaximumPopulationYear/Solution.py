class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        l = []
        for b, d in logs:
            l.append([b, 0])
            l.append([d-1, 1])
        l.sort()
        
        res, max_ = -1, -1
        cur = 0
        for y, z in l:
            if z == 0:
                cur += 1
            else:
                cur -= 1
            if cur > max_:
                res = y
                max_ = cur
        return res
    
            