class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        count = 0
        for l, w in rectangles:
            cur = min(l,w)
            if cur == res:
                count += 1
            elif cur > res:
                res = cur
                count = 1
        return count
    