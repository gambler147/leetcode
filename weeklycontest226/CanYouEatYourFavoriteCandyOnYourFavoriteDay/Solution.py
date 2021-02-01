class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # prefix
        n = len(candiesCount)
        prefix = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            prefix[i] = prefix[i-1] + candiesCount[i-1]
        
        res = []
        for tp, d, cap in queries:
            # if we can cosume all candies plus 1 before type tp candies in (d+1) days and our total
            # candies including type tp can cover 1 candies per day in d days, it is true
            if prefix[tp] < (d+1) * cap and prefix[tp+1] > d:
                res.append(True)
            else:
                res.append(False)
        return res
            
        