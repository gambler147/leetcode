class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        cur, res = 1, 0
        for i in range(n):
            if i > 0 and prices[i] == prices[i-1] - 1:
                cur += 1
            else:
                cur = 1
            res += cur
        return res
            
