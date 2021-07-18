class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        added = 0
        cur = 0
        for nxt in rungs:
            added += (nxt-cur-1)//dist
            cur = nxt
        return added
