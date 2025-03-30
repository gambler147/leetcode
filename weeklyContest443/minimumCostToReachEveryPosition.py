class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res = []
        curMin = float('inf')
        for c in cost:
            curMin = min(c, curMin)
            res.append(curMin)
        return res

