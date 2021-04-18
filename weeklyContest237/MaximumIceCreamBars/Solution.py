class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for c in costs:
            if coins < c:
                return res
            res+=1
            coins-=c
        return res
    