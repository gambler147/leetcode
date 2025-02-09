class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)
        
        def canAchieve(min_val):
            vals = [0 for _ in range(n)]
            steps_left = m
            for i in range(n):
                if i == n-1 and vals[i] >= min_val:
                    return True
                    
                vals[i] += points[i]
                steps_left -= 1
                vals_req = max(0, min_val - vals[i] )
                steps_req = (vals_req + points[i] - 1 ) // points[i]
                steps_left -= 2 * steps_req
                
                if steps_left < 0:
                    return False

                if i < n-1:
                    vals[i+1] += points[i+1] * steps_req

            return True

        i, j = 0, min(points) * m + 1
        while i < j:
            mid = (i+j+1) // 2
            if canAchieve(mid):
                i = mid
            else:
                j = mid-1
        return i
                
