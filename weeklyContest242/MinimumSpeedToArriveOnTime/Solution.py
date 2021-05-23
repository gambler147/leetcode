class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # binary search
        n = len(dist)
        MAX = 10**7
        
        def get_total_time(dist, speed):
            n = len(dist)
            total = 0
            for i in range(n-1):
                total += int(math.ceil(dist[i]/speed))
            total += dist[-1]/speed
            return total
        
        # speed can take from 1 to MAX+1, inclusive
        i, j = 1, MAX
        while i < j:
            m = (i+j) >> 1
            total = get_total_time(dist, m)
            if total <= hour:
                j = m
            else:
                i = m+1
        
        total = get_total_time(dist, i)
        if total <= hour:
            return i
        
        return -1