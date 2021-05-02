class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort the intervals and queries from small to large
        # we use a min-heap of intervals with [size, right]
        # we iterate the queries and check if the top interval in heap should be removed
        # until no intervals in heap or top interval is valid. Then the top interval size
        # is the answer to corresponding query
        
        # Total time complexity: O(nlog(n) + qlog(q)) where n is the length of intervals 
        # and q is the queries length

        # sort queries by the value
        intervals.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1])
        q = len(queries)
        
        # create a heap to store the [size, right] of intervals
        h = []
        # result 
        res = [None for _ in range(q)]
        
        # iterate queries from smallest to largest
        k = 0 # index in intervals
        for i, v in queries:
            # add or remove endpoints that before v
            while k < len(intervals) and intervals[k][0] <= v:
                l, r = intervals[k]
                size = r - l + 1
                # check if it is left endpoint (add to heap) or right endpoint (to be removed)
                heapq.heappush(h, [size, r])
                k += 1
            # delete intervals from heap if their right endpoints are smaller than current query value
            while h and h[0][1] < v:
                heapq.heappop(h)
            # get result
            res[i] = h[0][0] if h else -1
        return res
            
            