class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # get the lower and upper bound of each number, we use a min heap to record all 
        # pairs of (lower, upper), pop the smallest lower bound and double it if possible
        bounds = []
        for i, num in enumerate(nums):
            if num%2 == 1:
                num*=2
            upper = num
            while num%2 == 0:
                num //= 2
            lower = num
            heapq.heappush(bounds, (lower, upper))
            
        upper = max(x[0] for x in bounds)
        lower = min(x[0] for x in bounds)
        res = upper - lower
        while bounds[0][0] < bounds[0][1]:
            # we can still pop the lowest lower bound and double it
            l, u = heapq.heappop(bounds)
            heapq.heappush(bounds, (l * 2, u))
            upper = max(upper, l * 2)
            lower = bounds[0][0]
            res = min(res, upper - lower)
        return res
