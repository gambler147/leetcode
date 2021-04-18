class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res, ans = float('inf'), -1
        for idx, (i,j) in enumerate(points):
            if x == i or y == j:
                dis = abs(x-i) + abs(y-j)
                if dis < res:
                    res = dis
                    ans = idx
        return ans
                