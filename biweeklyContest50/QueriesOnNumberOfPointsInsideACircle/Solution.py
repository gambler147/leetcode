class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # brute force (O(nq))
        res = []
        for x,y,r in queries:
            cnt = 0
            for a,b in points:
                if (x-a)**2 + (y-b)**2 <= r**2:
                    cnt += 1
            res.append(cnt)
        return res
    